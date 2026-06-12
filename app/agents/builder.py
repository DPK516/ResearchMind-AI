from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_classic.agents import create_tool_calling_agent, AgentExecutor


from app.core.config import settings
from app.agents.tools import web_search, scrape_url


def get_llm() -> ChatMistralAI:
    """Factory function to instantiate the LLM securely and cleanly."""
    return ChatMistralAI(
        model=settings.model_name, 
        temperature=settings.temperature,
        api_key=settings.mistral_api_key
    )


def build_search_agent_executor() -> AgentExecutor:
    """Creates a fresh search agent for a new request."""
    llm = get_llm()
    tools = [web_search]
    
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a specialized research assistant. Use the web_search tool to find accurate and recent information."),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}")
    ])
    
    agent = create_tool_calling_agent(llm, tools, prompt)
    
    
    return AgentExecutor(agent=agent, tools=tools, handle_parsing_errors=True)


def build_reader_agent_executor() -> AgentExecutor:
    """Creates a fresh reader agent for deep scraping."""
    llm = get_llm()
    tools = [scrape_url]
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a deep-dive reading assistant. Use the scrape_url tool to extract knowledge from specific URLs."),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}")
    ])
    
    agent = create_tool_calling_agent(llm, tools, prompt)
    return AgentExecutor(agent=agent, tools=tools, handle_parsing_errors=True)


def get_writer_chain():
    """Creates a chain to format the final report."""
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
        ("human", "Topic: {topic}\n\nResearch Gathered:\n{research}\n\nStructure the report as:\n- Introduction\n- Key Findings\n- Conclusion\n- Sources")
    ])
    return prompt | get_llm() | StrOutputParser()

def get_risk_assessment_chain():
    """Builds the Risk Assessment Analyst chain."""
    llm = get_llm()
    
    prompt = ChatPromptTemplate.from_messages([
        (
            "system", 
            "You are an elite Enterprise Risk Analyst. Your job is to review AI-generated intelligence reports and provide a strictly professional 'Risk & Bias Assessment' disclaimer. "
            "Do NOT score, grade, or evaluate the quality of the report. "
            "Instead, output a concise, highly professional summary covering:\n"
            "1. Potential Biases (Are the sources likely leaning a certain way?)\n"
            "2. Unverified Claims (What assumptions is the report making?)\n"
            "3. Strategic/Market Risks (What external factors could invalidate this intelligence?)\n\n"
            "Keep the tone objective, clinical, and executive."
        ),
        ("human", "Review this intelligence payload:\n\n{report}")
    ])
    
    return prompt | llm | StrOutputParser()