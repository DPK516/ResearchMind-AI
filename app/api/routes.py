from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.research import ResearchService


router = APIRouter()


class ResearchRequest(BaseModel):
    topic: str

class ResearchResponse(BaseModel):
    topic: str
    search_results: str
    scraped_content: str
    report: str
    feedback: str


@router.post("/research", response_model=ResearchResponse)
async def run_research(request: ResearchRequest):
    """
    Receives a topic, runs the multi-agent pipeline, and returns the report.
    """
    try:
        
        service = ResearchService()
        
        
        result = await service.execute_pipeline(request.topic)
        
        return result
    except Exception as e:
        
        raise HTTPException(status_code=500, detail=str(e))