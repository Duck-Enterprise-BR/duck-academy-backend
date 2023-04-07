from api.database.database_base import Session
from api.base.base_models import PlansModel, PlansDetailsModel, PlansRelationshipModel
from api.module.plans_module.plans.dtos.plans_create import PlansCreateDto, PlansUpdateDto

""" for x in session.query( Department, Employee)
    .filter(Link.department_id == Department.id, Link.employee_id == Employee.id)
    .order_by(Link.department_id)
    .all():
   print ("Department: {} Name: {}".format(x.Department.name, x.Employee.name)) """

class PlansRepository:
    def list(self):
        items = []
        session = Session()
        query = session.query(PlansRelationshipModel,PlansModel).filter(PlansRelationshipModel.plan_id == PlansModel.id, PlansRelationshipModel.plans_details_id == PlansDetailsModel.id).all()

        print(query)

        for x in query:
            print("{}".format(x.PlansModel.name))
            items.append({
                "plan": x.PlansModel.name,
                "plan_ids": x.PlansRelationshipModel.plans_details_id
            })

        return items
        
    
    
    def save(self, item: PlansCreateDto):
        session = Session()
        data = PlansModel(name=item.name, description=item.description)
        session.add(data)
        session.commit()
        session.refresh(data)
        return data
    
    def update(self, id: str, item: PlansUpdateDto):
        session = Session()
        oldData = session.query(PlansModel).filter_by(id=id).one()
        oldData.name = item.name
        oldData.description = item.description
        session.commit()
        return item
    
    def checkAlreadyCreateById(self, id):
        session = Session()
        return int(session.query(PlansModel)
        .filter(PlansModel.id == id)
        .count())

    def checkAlreadyCreate(self, name: str):
        session = Session()
        return int(session.query(PlansModel)
        .filter(PlansModel.name == name)
        .count())
    
    def deleteById(self, id):
        session = Session()
        oldData = session.query(PlansModel).filter_by(id=id).one()
        oldData.enabled = False
        session.commit()
        return True