from api.module.plans_module.plans_relationship.dtos.relationship_create import RelationshipCreateDto
from api.module.plans_module.plans.plans_repository import PlansRepository
from api.module.plans_module.plansDetails.plans_details_repository import PlansDetailsRepository
from api.module.plans_module.plans_relationship.plans_relationship_repository import PlansRelationshipRepository
from api.utils.uuid import UuidUtils
from api.utils.response_message import ResponseMessage

class PlansRelationshipService:
    plansRepository = PlansRepository()
    plansDetailsRepository = PlansDetailsRepository()
    plansRelationshipRepository = PlansRelationshipRepository()

    def list(self):
        return self.plansRelationshipRepository.list()
    
    def create(self, item: RelationshipCreateDto):
        valid_plans_id = UuidUtils.validUuid(item.plan_id)
        valid_plans_id_details = UuidUtils.validUuid(item.plans_details_id)

        if valid_plans_id == False:
            ResponseMessage.ErrorHandleResponse(400, { 'plan_id': ResponseMessage.getInvalidId() })
 
        if valid_plans_id_details == False:
            ResponseMessage.ErrorHandleResponse(400, { 'plans_id_details': ResponseMessage.getInvalidId() })

        check_plans_id = self.plansRepository.checkAlreadyCreateById(item.plan_id)
        check_plans_details_id = self.plansDetailsRepository.count_by_id(item.plans_details_id)

        if check_plans_id == 0:
            ResponseMessage.ErrorHandleResponse(404, { "plan_id": ResponseMessage.getNotFound() })

        if check_plans_details_id == 0:
            ResponseMessage.ErrorHandleResponse(404, { "plans_id_details": ResponseMessage.getNotFound() })

        check_already_create = self.plansRelationshipRepository.check_already_create_relationship(item.plan_id, item.plans_details_id)

        if check_already_create == 1:
            ResponseMessage.ErrorHandleResponse(400, ResponseMessage.getAlreadyCreated())

        return self.plansRelationshipRepository.save(item)