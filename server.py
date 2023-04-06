from fastapi import FastAPI
from api.company import company_controller
from config import Settings

settings = Settings()
app = FastAPI()

app.include_router(company_controller.router)