from pydantic import BaseModel

class PermissionCreateDto(BaseModel):
    name: str
    tag: str