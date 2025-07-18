from typing import List, Optional
from datetime import datetime
import uuid
from app.models.user import UserCreate, UserResponse

class UserService:
    def __init__(self):
        # In-memory storage for demo purposes
        # In production, you'd use a real database
        self.users = []
    
    async def create_user(self, user: UserCreate) -> UserResponse:
        """Create a new user"""
        user_id = str(uuid.uuid4())
        now = datetime.utcnow()
        
        # In production, hash the password before storing
        user_data = user.dict(exclude={"password"})
        user_data.update({
            "id": user_id,
            "is_active": True,
            "created_at": now
        })
        
        user_response = UserResponse(**user_data)
        self.users.append(user_response)
        return user_response
    
    async def get_all_users(self) -> List[UserResponse]:
        """Get all users"""
        return self.users
    
    async def get_user_by_id(self, user_id: str) -> Optional[UserResponse]:
        """Get a user by ID"""
        for user in self.users:
            if user.id == user_id:
                return user
        return None
