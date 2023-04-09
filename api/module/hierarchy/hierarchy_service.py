from api.module.hierarchy.hierarchy_repository import HierarchyRepository
from api.module.hierarchy.dto.hierarchy_create import HierarchyCreateDto, HierarchyUpdateDto
from api.utils.response_message import ResponseMessage
from api.utils.uuid import UuidUtils

class HierarchyService:
    hierarchyRepository = HierarchyRepository()

    def list(self):
        return self.hierarchyRepository.list()
    
    def save(self, item: HierarchyCreateDto):
        self.checkName(item.name)

        return item
    
    def update(self, id, item: HierarchyUpdateDto):
        self.checkIfValidId(id)
        self.checkName(item.name)

        return self.hierarchyRepository.update(id, item)
    
    def delete(self, id: str):
        self.checkIfValidId(id)

        return self.hierarchyRepository.delete_by_id(id)
    
    def checkName(self, name: str):
        checkName = self.hierarchyRepository.count_by_field("name", name)

        if checkName >= 1:
            ResponseMessage.ErrorHandleResponse(400, { "name": ResponseMessage.getAlreadyCreated() })

    def checkIfValidId(self, id):
        checkValidUuid = UuidUtils.validUuid(id)

        if checkValidUuid == False:
            ResponseMessage.ErrorHandleResponse(400, { "id": ResponseMessage.getInvalidId() })

        checkId = self.hierarchyRepository.count_by_id(id)

        if checkId == 0:
            ResponseMessage.ErrorHandleResponse(404, { "id": ResponseMessage.getNotFound() })