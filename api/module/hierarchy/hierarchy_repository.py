from api.base.base_repository import BaseRepository
from api.base.base_models import HierarchyModel

class HierarchyRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__(HierarchyModel, "hierarchy")