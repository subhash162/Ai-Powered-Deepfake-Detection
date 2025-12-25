from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DetectionBase(BaseModel):
    image_name: str
    image_size: int

class DetectionCreate(DetectionBase):
    image_path: str

class DetectionUpdate(BaseModel):
    is_ai_generated: Optional[bool] = None
    confidence_score: Optional[float] = None
    model_used: Optional[str] = None
    detection_details: Optional[str] = None

class DetectionResponse(DetectionBase):
    id: int
    user_id: int
    image_path: str
    is_ai_generated: Optional[bool]
    confidence_score: Optional[float]
    model_used: Optional[str]
    detection_details: Optional[str]
    created_at: datetime
    processed_at: Optional[datetime]
    
    class Config:
        from_attributes = True

class DetectionList(BaseModel):
    total: int
    items: list[DetectionResponse]