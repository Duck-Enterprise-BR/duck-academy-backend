from api.base.base_repository import BaseRepository
from api.base.base_models import PermissionModel

class PermissionRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__(PermissionModel, "permission")