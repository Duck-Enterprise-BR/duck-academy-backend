from api.base.base_repository import BaseRepository

class BaseService:
    def __init__(self, repository: BaseRepository) -> None:
        self.repository = repository

    def list(self):
        return self.repository.list(self)
    
    def delete(self, id: str):
        return self.repository.delete_by_id(id)
