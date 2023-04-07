from pydantic import BaseModel

class RelationshipCreateDto(BaseModel):
    plan_id: str
    plans_details_id: str