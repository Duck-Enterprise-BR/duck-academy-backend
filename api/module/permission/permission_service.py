from api.module.permission.permission_repository import PermissionRepository
from api.module.permission.dto.permission_create import PermissionCreateDto
from api.utils.response_message import ResponseMessage
from api.utils.uuid import UuidUtils

class PermissionService:
    permissionRepository = PermissionRepository()

    def list(self):
        return self.permissionRepository.list()
    
    def create(self, item: PermissionCreateDto):
        checkName = self.permissionRepository.count_by_field("name", item.name)
        checkTag = self.permissionRepository.count_by_field("tag", item.tag)

        if(checkName >= 1):
            raise ResponseMessage.ErrorHandleResponse(400, { "name": ResponseMessage.getAlreadyCreated() })
        
        if(checkTag >= 1):
            raise ResponseMessage.ErrorHandleResponse(400, { "tag": ResponseMessage.getAlreadyCreated() })
        
        return self.permissionRepository.save(item)
    
    def update(self, id: str, item: PermissionCreateDto):
        self.validateId(id)
        self.validateFields(item.name, item.tag, id)

        return self.permissionRepository.update(id, item)
    
    def delete(self, id):
        self.validateId(id)
        
        return self.permissionRepository.delete_by_id(id)
    
    def validateId(self, id):
        validUuid = UuidUtils.validUuid(id)

        if validUuid is False:
            raise ResponseMessage.ErrorHandleResponse(400, { "id": ResponseMessage.getInvalidId() })
        
        checkExists = self.permissionRepository.check_already_create_by_id(id)

        if checkExists <= 0:
            raise ResponseMessage.ErrorHandleResponse(404, { "id": ResponseMessage.getNotFound() })

    def validateFields(self, name: str, tag: str, id: str):
        checkName = self.permissionRepository.count_by_field("name", name, id)
        checkTag = self.permissionRepository.count_by_field("tag", tag, id)

        if(checkName >= 1):
            raise ResponseMessage.ErrorHandleResponse(400, { "name": ResponseMessage.getAlreadyCreated() })
        
        if(checkTag >= 1):
            raise ResponseMessage.ErrorHandleResponse(400, { "tag": ResponseMessage.getAlreadyCreated() })
