import asyncio
import aiohttp
from bs4 import BeautifulSoup
from tavily import AsyncTavilyClient
from langchain.tools import tool
from pydantic import BaseModel, Field

from app.core.config import settings

tavily_client = AsyncTavilyClient(api_key=settings.tavily_api_key)


class WebSearchInput(BaseModel):
    query: str = Field(description="The exact search query to look up on the internet.")

@tool("web_search", args_schema=WebSearchInput)
async def web_search(query: str) -> str:
    """Search the web for recent and reliable information on a topic. Returns Titles, URLs, and snippets."""
    try:
        
        results = await tavily_client.search(query=query, max_results=5)
        
        out = []
        for r in results.get('results', []):
            out.append(f"Title: {r['title']}\nURL: {r['url']}\nSnippet: {r['content'][:300]}\n")
            
        return "\n----\n".join(out)
    except Exception as e:
        
        return f"Search service is temporarily unavailable. Error: {str(e)}"


class ScrapeUrlInput(BaseModel):
    url: str = Field(description="The valid HTTP/HTTPS URL of the website to scrape.")

@tool("scrape_url", args_schema=ScrapeUrlInput)
async def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading."""
    
    timeout = aiohttp.ClientTimeout(total=settings.timeout_seconds)
    
    try:
        
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(url, headers={"User-Agent": "Mozilla/5.0"}) as resp:
                resp.raise_for_status()
                html_content = await resp.text()
                
                soup = BeautifulSoup(html_content, "html.parser")
                
                
                for tag in soup(["script", "style", "nav", "footer", "header"]):
                    tag.decompose()
                
                text = soup.get_text(separator=" ", strip=True)
                return text[:3000] 
                
    except asyncio.TimeoutError:
        return "Error: The website took too long to respond."
    except Exception as e:
        return f"Error: Could not extract content from the provided URL. {str(e)}"