import uuid

class UuidUtils:
    def getUuid():
        return uuid.uuid4()
    
    def validUuid(id: str):
        try:
            uuid.UUID(id, version=4)
            return True
        except ValueError:
            return False