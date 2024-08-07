from typing import List

from db.create import NewDB, SessionLocal
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

app = FastAPI()


# Pydantic model for user input
class UserCreate(BaseModel):
    name: str
    email: str


# Pydantic model for user output
class UserOut(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        # Object-Relational Mapping --> PyDantic handle SQLAlchemy objects
        orm_mode = True


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/user/{user_id}", response_model=UserOut)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(NewDB).filter(NewDB.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.post("/users/", response_model=List[UserOut])
def create_users(users: List[UserCreate], db: Session = Depends(get_db)):
    created_users = []
    for user in users:
        db_user = NewDB(name=user.name, email=user.email)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        created_users.append(db_user)
    return created_users
