from api.base.base_repository import BaseRepository
from api.base.base_models import PlansDetailsModel

class PlansDetailsRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__(PlansDetailsModel)
    