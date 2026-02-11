from fastapi import FastAPI,Depends,HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
DATABASE_URL = "postgresql://postgres:1234@localhost:5432/test_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base=declarative_base()
app=FastAPI()

class UserDB(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    age=Column(Integer)
Base.metadata.create_all(bind=engine)

class User(BaseModel):
    name:str
    age:int 

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
# GET user by ID
@app.get("/users")
def get_users(db:Session=Depends(get_db)):
    return db.query(UserDB).all()

# POST create user
@app.post("/users")
def create_user(user:User,db:Session=Depends(get_db)):
    db_user=UserDB(name=user.name,age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/{user_id}")
def get_user(user_id:int,db:Session=Depends(get_db)):
    user=db.query(UserDB).filter(UserDB.id==user_id).first()
    if not user:
        raise HTTPException(status_code=404,detail="user not found")
    return user

# DELETE user by ID
@app.delete("/users/{user_id}")
def delete_user(user_id:int,db:Session=Depends(get_db)):
    user=db.query(UserDB).filter(UserDB.id==user_id).first()
    if not user:
        raise HTTPException(status_code=404,detail="user not found")
    db.delete(user)
    db.commit()
    return {"message":"deleted successfully","user":user_id}