from fastapi import FastAPI
from api.module.company import company_controller
from api.module.plans_module.plans import plans_controller
from api.module.plans_module.plansDetails import plans_details_controller
from config import Settings

settings = Settings()
app = FastAPI()

app.include_router(company_controller.router)
app.include_router(plans_controller.plansRouter)
app.include_router(plans_details_controller.plans_details_routes_api)