from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class AvatarBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    personality_traits: Optional[str] = Field(None, max_length=1000)
    voice_settings: Optional[dict] = None
    appearance_settings: Optional[dict] = None

class AvatarCreate(AvatarBase):
    pass

class AvatarResponse(AvatarBase):
    id: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
