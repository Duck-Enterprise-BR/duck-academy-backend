from fastapi import FastAPI
from api.module.company import company_controller
from api.module.plans_module.plans import plans_controller
from api.module.plans_module.plansDetails import plans_details_controller
from api.module.plans_module.plans_relationship import plans_relationship_controller
from api.module.hierarchy import hierarchy_controller
from api.module.permission import permission_controller
from api.midlleware.api_token_middleware import api_token_middleware
from config import Settings

settings = Settings()
app = FastAPI()

app.middleware("http")(api_token_middleware)
app.include_router(company_controller.router)
app.include_router(plans_controller.plansRouter)
app.include_router(plans_details_controller.plans_details_routes_api)
app.include_router(plans_relationship_controller.plans_relationship_router)
app.include_router(hierarchy_controller.hierarchy_api_routes)
app.include_router(permission_controller.routes)