from api.module.hierarchy.hierarchy_service import HierarchyService
from api.module.hierarchy.dto.hierarchy_create import HierarchyCreateDto, HierarchyUpdateDto
from fastapi import APIRouter

hierarchy_api_routes = APIRouter()
hierarchyService = HierarchyService()
hierarchy_api_name = "/hierarchy"

@hierarchy_api_routes.get(hierarchy_api_name)
def list():
    return hierarchyService.list()

@hierarchy_api_routes.post(hierarchy_api_name)
def save(item: HierarchyCreateDto):
    return hierarchyService.save(item)

@hierarchy_api_routes.put("/hierarchy/{id}")
def update(id: str, item: HierarchyUpdateDto):
    return hierarchyService.update(id, item)

@hierarchy_api_routes.delete("/hierarchy/{id}")
def delete(id):
    return hierarchyService.delete(id)