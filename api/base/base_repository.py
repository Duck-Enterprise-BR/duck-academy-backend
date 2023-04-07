from api.database.database_base import Session

class BaseRepository:
    def __init__(self, model) -> None:
        self.__model = model

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
        print(id)
        try:
            session = Session()
            return int(session.query(self.__model).filter_by(id=id).count())
        except:
            return 0
    
    def delete_by_id(self, id):
        session = Session()
        oldData = session.query(self.__model).filter_by(id=id).one()
        oldData.enabled = False
        session.commit()
        return True