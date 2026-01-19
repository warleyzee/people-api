from fastapi import FastAPI
from app.routes.people_routes import router as people_router

app = FastAPI(title="People API")

app.include_router(people_router)
