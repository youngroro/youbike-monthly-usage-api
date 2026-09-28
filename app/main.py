from fastapi import FastAPI

from app.database import Base, engine
from app.routers import  monthly_usage

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Taipei YouBike Monthly Usage API",
    description="RESTful API for Taipei YouBike monthly usage Open Data",
    version="1.0.0",
)

app.include_router(monthly_usage.router)


@app.get("/")
def root():
    return {
        "message": "Taipei YouBike Monthly Usage API"
    }