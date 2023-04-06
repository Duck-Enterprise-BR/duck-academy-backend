from api.module.plans.dtos.plans_create import PlansCreateDto, PlansUpdateDto
from api.module.plans.plans_repository import PlansRepository
from api.utils.uuid import UuidUtils
from api.utils.response_message import ResponseMessage
from fastapi import HTTPException

class PlansService:
    responseMessage = ResponseMessage()
    plansRepository = PlansRepository()
    uuidUtils = UuidUtils()
    
    def list(self):
        return self.plansRepository.list()
    
    def create(self, item: PlansCreateDto):
        checkAlreadyCreate = self.plansRepository.checkAlreadyCreate(item.name)

        if(checkAlreadyCreate >= 1):
            raise HTTPException(status_code=400, detail=self.responseMessage.getAlreadyCreated())

        return self.plansRepository.save(item)
    
    def update(self, id: str, item: PlansUpdateDto):
        self.checkIfValidId(id)

        return self.plansRepository.update(id, item)
    
    def deleteById(self, id: str):
        self.checkIfValidId(id)
        return self.plansRepository.deleteById(id)
    
    def checkIfValidId(self, id: str):
        validUuid = self.uuidUtils.validUuid(id)

        if(validUuid == False):
            raise HTTPException(status_code=400, detail=self.responseMessage.getInvalidParams())

        checkAlreadyExists = self.plansRepository.checkAlreadyCreateById(id)

        if (checkAlreadyExists == 0):
            raise HTTPException(status_code=404, detail=self.responseMessage.getNotFound())

