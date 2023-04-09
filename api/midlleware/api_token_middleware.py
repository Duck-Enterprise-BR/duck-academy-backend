from fastapi import Request, HTTPException
from config import Settings

settings = Settings()

async def api_token_middleware(request: Request, call_next):
    access_token = request.headers.get("access_token")
    access_token_valid = settings.access_token

    if access_token is None:
        raise HTTPException(status_code=401, detail='Unauthorized')
    
    if access_token_valid != access_token:
        raise HTTPException(status_code=401, detail='Unauthorized')
    
    response = await call_next(request)
    return response
