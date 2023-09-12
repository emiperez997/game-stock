import uvicorn
from fastapi import FastAPI

# Import scripts
from src.scripts.initialize_db import initialize_db

# Import router
from src.routes.index_router import router

# Cors config
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Swagger configuration
app.title = "Steam clone API"
app.description = "API for Steam clone"
app.version = "0.0.0"


# Cors config
# Url of frontend
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

# Include router
app.include_router(router, prefix="/api")
