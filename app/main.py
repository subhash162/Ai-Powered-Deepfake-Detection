from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from app.config import settings
from app.api.v1.router import api_router
from app.db.session import engine
from app.db.base import Base

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_PREFIX}/openapi.json"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this properly in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_PREFIX)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from app.config import settings
from app.api.v1.router import api_router
from app.db.session import engine
from app.db.base import Base

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_PREFIX}/openapi.json"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this properly in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_PREFIX)

@app.get("/")
async def root():
    """API information"""
    return {
        "message": f"{settings.PROJECT_NAME} v{settings.VERSION}",
        "status": "operational",
        "timestamp": datetime.utcnow().isoformat(),
        "endpoints": {
            "auth": {
                "signup": f"{settings.API_V1_PREFIX}/auth/signup",
                "login": f"{settings.API_V1_PREFIX}/auth/login",
                "token": f"{settings.API_V1_PREFIX}/auth/token"
            },
            "detection": {
                "upload": f"{settings.API_V1_PREFIX}/detections/upload",
                "list": f"{settings.API_V1_PREFIX}/detections/",
                "get": f"{settings.API_V1_PREFIX}/detections/{{id}}",
                "update": f"{settings.API_V1_PREFIX}/detections/{{id}}",
                "delete": f"{settings.API_V1_PREFIX}/detections/{{id}}"
            },
            "user": {
                "profile": f"{settings.API_V1_PREFIX}/users/me"
            }
        },
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}
