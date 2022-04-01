

# FastAPI
from fastapi import FastAPI
from routes.user import user
app = FastAPI(
    title = "My first API",
    description = "My first API with SQL",
    version = "0.0.1",
    openapi_tags=[{
        "name": "Users",
        "description": "users routes"
    }]
)
app.include_router(user)
