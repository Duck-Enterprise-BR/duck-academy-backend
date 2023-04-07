from fastapi import APIRouter
from api.module.plansDetails import plans_details_service
from api.module.plansDetails.dtos.plans_details_dto import PlansDetailsCreateDto, PlansDetailsUpdateDto

plan_details_routes_name = "/plans-details"
plans_details_routes_api = APIRouter()
plansDetailsService = plans_details_service.PlansDetailsService()

@plans_details_routes_api.get(plan_details_routes_name)
def list():
    return plansDetailsService.list()

@plans_details_routes_api.post(plan_details_routes_name)
def create(item: PlansDetailsCreateDto):
    return plansDetailsService.create(item)

@plans_details_routes_api.put("/plans-details/{id}")
def update(id: str, item: PlansDetailsUpdateDto):
    return plansDetailsService.update(id, item)

@plans_details_routes_api.delete("/plans-details/{id}")
def delete_by_id(id: str):
    return plansDetailsService.delete(id)