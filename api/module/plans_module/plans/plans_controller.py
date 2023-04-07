from fastapi import APIRouter
from api.module.plans_module.plans.plans_service import PlansService
from api.module.plans_module.plans.dtos.plans_create import PlansCreateDto, PlansUpdateDto

planRouterPrefix = "/plans"
plansRouter = APIRouter()

@plansRouter.get(planRouterPrefix)
def list():
    plansService = PlansService()
    return plansService.list()

@plansRouter.post(planRouterPrefix)
def create(data: PlansCreateDto):
    plansService = PlansService()
    return plansService.create(data)

@plansRouter.put("/plans/{item_id}")
def update(item_id, item: PlansUpdateDto):
    plansService = PlansService()
    return plansService.update(item_id, item)

@plansRouter.delete("/plans/{item_id}")
def deleteById(item_id: str):
    plansService = PlansService()
    return plansService.deleteById(item_id)