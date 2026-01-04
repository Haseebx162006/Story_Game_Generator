from typing import Optional,List,Dict
from pydantic import BaseModel
from datetime import datetime   


class StoryJobBase(BaseModel):
    theme: str
    
    
class CreateStoryJobResponse(StoryJobBase):
    job_id: str
    created_at: datetime
    status: str
    story_id: Optional[int]= None
    completed_at: Optional[datetime]= None
    error: Optional[str]= None
    
    class Config:
        from_attributes = True
        
        
class StoryJobCreate(StoryJobBase):
    pass