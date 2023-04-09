from api.base.base_models import PlansRelationshipModel
from api.base.base_repository import BaseRepository
from api.database.database_base import Session

class PlansRelationshipRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__(PlansRelationshipModel, "plans_relationship")

    def check_already_create_relationship(self, plan_id: str, plan_details_id: str):
        session = Session()
        return session.query(PlansRelationshipModel)\
        .filter(PlansRelationshipModel.plan_id == plan_id)\
        .filter(PlansRelationshipModel.plans_details_id == plan_details_id)\
        .count()