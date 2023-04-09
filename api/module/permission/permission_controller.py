from api.module.permission.permission_service import PermissionService
from api.module.permission.dto.permission_create import PermissionCreateDto
from fastapi import APIRouter

routes = APIRouter()
permissionService = PermissionService()

@routes.get("/permission")
def list():
    return permissionService.list()

@routes.post("/permission")
def save(item: PermissionCreateDto):
    return permissionService.create(item)

@routes.put("/permission/{id}")
def update(id: str, item: PermissionCreateDto):
    return permissionService.update(id, item)

@routes.delete("/permission/{id}")
def delete(id):
    return permissionService.delete(id)
