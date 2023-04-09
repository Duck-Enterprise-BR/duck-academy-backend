from pydantic import BaseModel

class HierarchyCreateDto(BaseModel):
    name: str
    sub_tag: str
    level: int

class HierarchyUpdateDto(BaseModel):
    name: str
    sub_tag: str
    level: int