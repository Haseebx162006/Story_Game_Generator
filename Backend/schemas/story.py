from typing import Optional,List,Dict
from pydantic import BaseModel
from datetime import datetime
class StoryOptionSchema(BaseModel):
    text: str
    node_id: Optional[int]= None
    
class StoryNodeBase(BaseModel):
    content: str
    is_ending: bool = False
    is_winning_ending: bool = False
    
    
class completeStoryNodeSchema(StoryNodeBase):
    id: int
    options: List[StoryOptionSchema]=[]
    class Config:
        from_attributes = True

class StoryBase(BaseModel):
    title: str
    session_id: str
    class Config:
        from_attributes = True
class CreateStoryRequest(BaseModel):
    title: str
   
class CreateStoryResponse(StoryBase):
    id: int
    created_at: datetime
    root_node: completeStoryNodeSchema
    all_nodes: List[completeStoryNodeSchema]
    
    class Config:
        from_attributes = True