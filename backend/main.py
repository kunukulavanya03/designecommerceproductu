from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os
from database import get_db, engine
from models import Base, User
from auth import verify_token, create_access_token, hash_password, verify_password
from schemas import *
import logging

load_dotenv()

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="This_Project_Aims_To_Develop_A_Backend_Api_For_The_Designecommerceproductu_Platform,_Utilizing_Fastapi_And_Sqlalchemy_For_Efficient_Data_Handling_And_Management. API",
    description="Complete backend API for this_project_aims_to_develop_a_backend_api_for_the_designecommerceproductu_platform,_utilizing_fastapi_and_sqlalchemy_for_efficient_data_handling_and_management.",
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

security = HTTPBearer()

# Authentication dependency
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    user_id = verify_token(token)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user_id

@app.get("/")
def read_root():
    return {"message": "Welcome to This_Project_Aims_To_Develop_A_Backend_Api_For_The_Designecommerceproductu_Platform,_Utilizing_Fastapi_And_Sqlalchemy_For_Efficient_Data_Handling_And_Management. API", "status": "running"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "this_project_aims_to_develop_a_backend_api_for_the_designecommerceproductu_platform,_utilizing_fastapi_and_sqlalchemy_for_efficient_data_handling_and_management."}

# Authentication endpoints
@app.post("/auth/register")
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    # Check if user exists
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create new user
    hashed_password = hash_password(user_data.password)
    new_user = User(
        email=user_data.email,
        username=user_data.username,
        hashed_password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    # Create access token
    access_token = create_access_token(data={"sub": str(new_user.id)})
    return {"access_token": access_token, "token_type": "bearer", "user_id": new_user.id}

@app.post("/auth/login")
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_data.email).first()
    if not user or not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer", "user_id": user.id}

# API endpoints
@app.get("/api/items")
def get_items(db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    # Get all items
    try:
        items = db.query(Item).filter(Item.owner_id == current_user).all()
        return {"items": items, "total": len(items)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/items")
def create_item(item_data: ItemCreate, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    # Create new item
    try:
        new_item = Item(**item_data.dict(), owner_id=current_user)
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        return {"item": new_item, "message": "Item created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)