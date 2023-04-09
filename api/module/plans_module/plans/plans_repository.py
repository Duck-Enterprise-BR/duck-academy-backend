from api.database.database_base import Session
from api.base.base_models import PlansModel
from api.module.plans_module.plans.dtos.plans_create import PlansCreateDto, PlansUpdateDto
from sqlalchemy import text

class PlansRepository:
    def list(self):
        items = []
        session = Session()
        result = session.execute(text("""
        SELECT
            plan_id,
            plans.name as plan,
            json_agg(json_build_object('id', plans_details.id, 'name', plans_details.name)) AS details
        from plans_relationship
        INNER JOIN plans 
            ON plans_relationship.plan_id = plans.id
        INNER JOIN plans_details 
            ON plans_relationship.plans_details_id = plans_details.id
        GROUP BY plan_id, plan;
        """)
        )

        for row in result:
            items.append({
                "plan_id": row[0],
                "name": row[1],
                "details": row[2]
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