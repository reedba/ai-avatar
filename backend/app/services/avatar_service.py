from typing import List, Optional
from datetime import datetime
import uuid
from app.models.avatar import AvatarCreate, AvatarResponse

class AvatarService:
    def __init__(self):
        # In-memory storage for demo purposes
        # In production, you'd use a real database
        self.avatars = []
    
    async def create_avatar(self, avatar: AvatarCreate) -> AvatarResponse:
        """Create a new avatar"""
        avatar_id = str(uuid.uuid4())
        now = datetime.utcnow()
        
        avatar_data = avatar.dict()
        avatar_data.update({
            "id": avatar_id,
            "created_at": now,
            "updated_at": now
        })
        
        avatar_response = AvatarResponse(**avatar_data)
        self.avatars.append(avatar_response)
        return avatar_response
    
    async def get_all_avatars(self) -> List[AvatarResponse]:
        """Get all avatars"""
        return self.avatars
    
    async def get_avatar_by_id(self, avatar_id: str) -> Optional[AvatarResponse]:
        """Get an avatar by ID"""
        for avatar in self.avatars:
            if avatar.id == avatar_id:
                return avatar
        return None
    
    async def update_avatar(self, avatar_id: str, avatar_data: AvatarCreate) -> Optional[AvatarResponse]:
        """Update an existing avatar"""
        for i, avatar in enumerate(self.avatars):
            if avatar.id == avatar_id:
                updated_data = avatar_data.dict()
                updated_data.update({
                    "id": avatar_id,
                    "created_at": avatar.created_at,
                    "updated_at": datetime.utcnow()
                })
                
                updated_avatar = AvatarResponse(**updated_data)
                self.avatars[i] = updated_avatar
                return updated_avatar
        return None
    
    async def delete_avatar(self, avatar_id: str) -> bool:
        """Delete an avatar"""
        for i, avatar in enumerate(self.avatars):
            if avatar.id == avatar_id:
                del self.avatars[i]
                return True
        return False
