from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os
from database import get_db, engine
from models import Base
from schemas import *
import logging

load_dotenv()

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="This_Project_Aims_To_Develop_A_Backend_Api_For_The_Designecommerceproductu_Platform,_Utilizing_Fastapi_And_Sqlalchemy_For_Efficient_Data_Handling_And_Management. API",
    description="Backend API for this_project_aims_to_develop_a_backend_api_for_the_designecommerceproductu_platform,_utilizing_fastapi_and_sqlalchemy_for_efficient_data_handling_and_management.",
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
    return {"message": "Welcome to This_Project_Aims_To_Develop_A_Backend_Api_For_The_Designecommerceproductu_Platform,_Utilizing_Fastapi_And_Sqlalchemy_For_Efficient_Data_Handling_And_Management. API", "status": "running"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "this_project_aims_to_develop_a_backend_api_for_the_designecommerceproductu_platform,_utilizing_fastapi_and_sqlalchemy_for_efficient_data_handling_and_management."}

# API endpoints inferred from frontend


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)