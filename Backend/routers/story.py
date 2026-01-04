import uuid
from typing import Optional
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException,Cookie,Response,BackgroundTasks
from sqlalchemy.orm import Session


from db.database import get_db,session
from models.story import Story,StoryNode
from models.job import StoryJob
from schemas.story import(
    CreateStoryRequest,
    CreateStoryResponse,
    completeStoryNodeSchema
)

from schemas.job import CreateStoryJobResponse

router=APIRouter(
    prefix="/stories",
    tags=["stories"]
)
def get_session_id(session_id: Optional[str]=Cookie(None)):
    if session_id is None:
        session_id=str(uuid.uuid4())
    return session_id

@router.post("/create", response_model=CreateStoryResponse)
def create_story(
    request:CreateStoryRequest,
    background_tasks: BackgroundTasks,
    response: Response, 
    session_id: str= Depends(get_session_id),
    db: Session= Depends(get_db)
):
    response.set_cookie(key="session_id", value=session_id, httponly=True)
    job_id= str(uuid.uuid4())
    Job= StoryJob(
        job_id= job_id,
        session_id=session_id,
        theme=request.title,
        status="pending"
    )
    db.add(Job)
    db.commit()
    db.refresh(Job)
    
    
    #TODO: Add background task to generate story
    
    return Job

def generate_story_task(job_id:str,theme:str, session_id:str):

