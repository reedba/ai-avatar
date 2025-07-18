from fastapi import APIRouter, HTTPException
from typing import List
from app.models.avatar import AvatarCreate, AvatarResponse
from app.services.avatar_service import AvatarService

router = APIRouter()
avatar_service = AvatarService()

@router.post("/", response_model=AvatarResponse)
async def create_avatar(avatar: AvatarCreate):
    """Create a new AI avatar"""
    try:
        return await avatar_service.create_avatar(avatar)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[AvatarResponse])
async def get_avatars():
    """Get all avatars"""
    return await avatar_service.get_all_avatars()

@router.get("/{avatar_id}", response_model=AvatarResponse)
async def get_avatar(avatar_id: str):
    """Get a specific avatar by ID"""
    avatar = await avatar_service.get_avatar_by_id(avatar_id)
    if not avatar:
        raise HTTPException(status_code=404, detail="Avatar not found")
    return avatar

@router.put("/{avatar_id}", response_model=AvatarResponse)
async def update_avatar(avatar_id: str, avatar: AvatarCreate):
    """Update an existing avatar"""
    updated_avatar = await avatar_service.update_avatar(avatar_id, avatar)
    if not updated_avatar:
        raise HTTPException(status_code=404, detail="Avatar not found")
    return updated_avatar

@router.delete("/{avatar_id}")
async def delete_avatar(avatar_id: str):
    """Delete an avatar"""
    success = await avatar_service.delete_avatar(avatar_id)
    if not success:
        raise HTTPException(status_code=404, detail="Avatar not found")
    return {"message": "Avatar deleted successfully"}
