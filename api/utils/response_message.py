from fastapi import HTTPException
class ResponseMessage:
    def getAlreadyCreated():
        return "Already Created"
    
    def getInvalidParams():
        return "Invalid params"
    
    def getNotFound():
        return "Not found"
    
    def getInvalidId():
        return "Invalid id"
    
    def ErrorHandleResponse(status_code: int, message: dict[str, str]):
        raise HTTPException(status_code, message)