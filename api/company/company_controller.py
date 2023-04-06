from fastapi import APIRouter
from api.company import company_service
from api.company.dtos import company_dtos

router = APIRouter()
companyService = company_service.CompanyService

@router.get("/")
def list():
    return companyService.list()

@router.post("/")
def create(item: company_dtos.CompanyCreateDto):
    return companyService.create(item)

@router.put("/{item_id}")
def update(item_id: str, item: company_dtos.CompanyCreateDto):
    return companyService.update(item_id, item)

@router.delete("/{item_id}")
def delete(item_id):
    return companyService.delete(item_id)