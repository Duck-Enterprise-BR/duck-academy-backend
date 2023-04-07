from api.base.base_repository import BaseRepository
from api.module.plans_module.plansDetails.plans_details_model import PlansDetailsModel

class PlansDetailsRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__(PlansDetailsModel)
    