from pydantic import BaseModel

class PlansDetailsCreateDto(BaseModel):
    name: str

class PlansDetailsUpdateDto(BaseModel):
    name: str = ""