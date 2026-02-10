from fastapi import FastAPI
app = FastAPI()

# GET (path parameter)
@app.get("/users/{user_id}")
def get_users(user_id: int):
    return {"user_id": user_id}

# POST (query parameters)
@app.post("/users")
def create_user(name: str, age: int):
    return {
        "message": "user created",
        "user": {
            "name": name,
            "age": age
        }
    }

# DELETE (path parameter)
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return {
        "message": "deleted successfully",
        "user_id": user_id
    }

# PUT (FULL update using query params)
@app.put("/users/{user_id}")
def update_user(user_id: int, name: str, age: int):
    return {
        "message": "updated successfully",
        "user_id": user_id,
        "user": {
            "name": name,
            "age": age
        }
    }

# PATCH (PARTIAL update using query params)
@app.patch("/users/{user_id}")
def update_partially_user(
    user_id: int,
    name: str | None = None,
    age: int | None = None
):
    return {
        "message": "updated partially",
        "user_id": user_id,
        "updated_fields": {
            "name": name,
            "age": age
        }
    }