from api.module.plans_module.plansDetails.plans_details_repository import PlansDetailsRepository
from api.module.plans_module.plansDetails.dtos.plans_details_dto import PlansDetailsCreateDto, PlansDetailsUpdateDto
from api.utils.response_message import ResponseMessage
from api.utils.uuid import UuidUtils
from fastapi import HTTPException

class PlansDetailsService:
    plansDetailsRepository = PlansDetailsRepository()
    uuidUtils = UuidUtils()

    def list(self):
        return self.plansDetailsRepository.list()
    
    def create(self, item: PlansDetailsCreateDto):
        checkName = self.plansDetailsRepository.checkAlreadyCreate(item.name)
        
        if(checkName):
            raise HTTPException(400, ResponseMessage.getAlreadyCreated())

        return self.plansDetailsRepository.save(item)
    
    def update(self, id: str, item: PlansDetailsUpdateDto):
        validUuid = self.uuidUtils.validUuid(id)

        if(validUuid == False):
            raise HTTPException(400, ResponseMessage.getInvalidId())
        
        oldItem = self.plansDetailsRepository.get_by_id(id)

        if(oldItem == False):
            raise HTTPException(404, ResponseMessage.getNotFound())

        return self.plansDetailsRepository.update(id, item) 
    
    def delete(self, id: str):
        return self.plansDetailsRepository.delete_by_id(id)