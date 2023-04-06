from pydantic import BaseModel

class CompanyCreateDto(BaseModel):
    company_name: str