import logging

from app.agents.builder import (
    build_search_agent_executor, 
    build_reader_agent_executor, 
    get_writer_chain, 
    get_risk_assessment_chain
)

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class ResearchService:
    def __init__(self):
        self.search_executor = build_search_agent_executor()
        self.reader_executor = build_reader_agent_executor()
        self.writer_chain = get_writer_chain()
        self.risk_chain = get_risk_assessment_chain()

    def _clean_text(self, data) -> str:
        """
        Helper function to extract pure string text from complex LLM payload chunks.
        Protects the FastAPI layer from Pydantic Validation Errors.
        """
        if isinstance(data, str):
            return data
        
        # If the LLM returns a list of chunks, we extract the 'text' from each chunk
        if isinstance(data, list):
            extracted = []
            for item in data:
                if isinstance(item, dict) and "text" in item:
                    extracted.append(item["text"])
                else:
                    extracted.append(str(item))
            return "".join(extracted)
            
        return str(data)

    async def execute_pipeline(self, topic: str) -> dict:
        state = {"topic": topic}
        
        # --- STEP 1: Search ---
        logger.info(f"Step 1: Searching for topic: {topic}")
        search_resp = await self.search_executor.ainvoke({
            "input": f"Find recent, reliable and detailed information about: {topic}"
        })
        # Clean the output before saving it!
        state["search_results"] = self._clean_text(search_resp.get("output", ""))

        # --- STEP 2: Read ---
        logger.info("Step 2: Scraping top resources...")
        reader_resp = await self.reader_executor.ainvoke({
            "input": f"Based on these results: {state['search_results'][:800]}, pick the most relevant URL and scrape it."
        })
        state["scraped_content"] = self._clean_text(reader_resp.get("output", ""))

        # --- STEP 3: Write ---
        logger.info("Step 3: Drafting the final report...")
        research_combined = f"SEARCH:\n{state['search_results']}\n\nSCRAPED:\n{state['scraped_content']}"
        raw_report = await self.writer_chain.ainvoke({
            "topic": topic, 
            "research": research_combined
        })
        state["report"] = self._clean_text(raw_report)

        
        logger.info("Step 4: Executing risk assessment...")
        raw_feedback = await self.risk_chain.ainvoke({
            "report": state["report"]
        })
        state["feedback"] = self._clean_text(raw_feedback)

        logger.info("Pipeline complete!")
        return state