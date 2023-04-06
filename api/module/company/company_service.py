from api.module.company.dtos.company_dtos import CompanyCreateDto
from api.module.company.company_repository import CompanyRepository

class CompanyService:
    def list():
        companyRepository = CompanyRepository()
        return companyRepository.list()
    
    def create(item: CompanyCreateDto):
        companyRepository = CompanyRepository()
        data = companyRepository.create(item.company_name)
        return data
    
    def update(id: str, item: CompanyCreateDto):
        return item
    
    def delete(id: str):
        return { "message": "success" }
