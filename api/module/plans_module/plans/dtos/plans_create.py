from pydantic import BaseModel

class PlansCreateDto(BaseModel):
    name: str
    description: str = ""

class PlansUpdateDto(BaseModel):
    name: str = ""
    description: str = ""