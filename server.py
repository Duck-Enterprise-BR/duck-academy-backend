from fastapi import FastAPI
from api.module.company import company_controller
from api.module.plans_module.plans import plans_controller
from api.module.plans_module.plansDetails import plans_details_controller
from api.module.plans_module.plans_relationship import plans_relationship_controller
from api.module.hierarchy import hierarchy_controller  
from config import Settings

settings = Settings()
app = FastAPI()

app.include_router(company_controller.router)
app.include_router(plans_controller.plansRouter)
app.include_router(plans_details_controller.plans_details_routes_api)
app.include_router(plans_relationship_controller.plans_relationship_router)
app.include_router(hierarchy_controller.hierarchy_api_routes)