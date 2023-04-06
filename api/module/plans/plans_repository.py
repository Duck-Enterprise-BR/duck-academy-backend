from api.module.plans.plans_model import PlansModel
from api.database.database_base import Session
from api.module.plans.plans_model import PlansModel
from api.module.plans.dtos.plans_create import PlansCreateDto, PlansUpdateDto

class PlansRepository:
    def list(self):
        session = Session()
        return session.query(PlansModel).filter(PlansModel.enabled == True).all()
    
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
    
    def checkAlreadyCreateById(self, id: str):
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