from fastapi import APIRouter
from api.module.plans_module.plans_relationship.plans_relationship_service import PlansRelationshipService
from api.module.plans_module.plans_relationship.dtos.relationship_create import RelationshipCreateDto

plans_relationship_router = APIRouter()
plans_relationship_router_name = "/plans_relationship"
plansRelationshipService = PlansRelationshipService()

@plans_relationship_router.get(plans_relationship_router_name)
def list():
    return plansRelationshipService.list()

@plans_relationship_router.post(plans_relationship_router_name)
def create(item: RelationshipCreateDto):
    return plansRelationshipService.create(item)