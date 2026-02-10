from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

# GET user by ID
@app.get("/users/{user_id}")
def get_users(user_id:int):
    return {"user_id":user_id}

# Model for creating/updating a user
class User(BaseModel):
    name:str
    age:int 

# POST create user
@app.post("/users")
def create_user(user:User):
    return {"message":"started fastapi","user":user}

# DELETE user by ID
@app.delete("/users/{user_id}")
def delete_user(user_id:int):
    return {"message":"deleted successfully","user":user_id}

# PUT full update of user
@app.put("/users/{user_id}")
def update_user(user_id:int,user:User):
    return {"message":"updated successfully","user_id":user_id,"user":user}

# Model for partial update
class UpdateUser(BaseModel):
    name: str | None = None
    age: int | None = None

# PATCH partial update of user
@app.patch("/users/{user_id}")
def update_partially_user(user_id:int,user:UpdateUser):
    return {"message":"updated partially","user":user}