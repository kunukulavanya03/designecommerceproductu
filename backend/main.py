from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os
from database import get_db, engine
from models import Base
from schemas import *
from routes import router as api_router
import logging

load_dotenv()

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="This_Project_Aims_To_Develop_A_Backend_Api_For_The_Designecommerceproductu_Platform_Using_Fastapi_And_Sqlalchemy,_With_Authentication_Via_Jwt. API",
    description="Backend API for this_project_aims_to_develop_a_backend_api_for_the_designecommerceproductu_platform_using_fastapi_and_sqlalchemy,_with_authentication_via_jwt.",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to This_Project_Aims_To_Develop_A_Backend_Api_For_The_Designecommerceproductu_Platform_Using_Fastapi_And_Sqlalchemy,_With_Authentication_Via_Jwt. API", "status": "running"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "this_project_aims_to_develop_a_backend_api_for_the_designecommerceproductu_platform_using_fastapi_and_sqlalchemy,_with_authentication_via_jwt."}

# API endpoints inferred from frontend
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)