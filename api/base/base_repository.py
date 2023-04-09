from api.database.database_base import Session
from sqlalchemy import text

class BaseRepository:
    def __init__(self, model, table: str) -> None:
        self.__model = model
        self.table = table

    def list(self):
        session = Session()
        return session.query(self.__model)\
        .filter(self.__model.enabled == True)\
        .all()
    
    def save(self, item):
        session = Session()
        print(item)
        data = self.__model(item)
        session.add(data)
        session.commit()
        session.refresh(data)
        return data
    
    def update(self, id: str, item):
        session = Session()
        oldData = session.query(self.__model).filter_by(id=id).one()

        for key, value in item:
            setattr(oldData, key, value)

        session.commit()
        return item
    
    def check_already_create_by_id(self, id: str):
        session = Session()
        return int(session.query(self.__model)
        .filter(self.__model.id == id)
        .count())

    def check_already_create(self, name: str):
        session = Session()
        return int(session.query(self.__model)
        .filter(self.__model.name == name)
        .count())
    
    def get_by_id(self, id: str):
        try:
            session = Session()
            print(self.__model)
            return session.query(self.__model).filter(self.__model.id == id).one()
        except:
            return {}
    
    def count_by_id(self, id):
        try:
            session = Session()
            return int(session.query(self.__model).filter_by(id=id).count())
        except:
            return 0
        
    def count_by_field(self, field, value):
        try:
            session = Session()
            query = {}
            query[field] = value
            query = text("SELECT COUNT(*) FROM {} where {} = '{}' AND enabled='t';".format(self.table, field, value))
            resultQuery = session.execute(query)

            for row in resultQuery:
                return int(str(row._data)[1])
        except:
            return 0
    
    def delete_by_id(self, id):
        session = Session()
        oldData = session.query(self.__model).filter_by(id=id).one()
        oldData.enabled = False
        session.commit()
        return True