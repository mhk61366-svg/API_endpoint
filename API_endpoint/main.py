from fastapi import FastAPI, HTTPException
from service import UserService
from repository import InMemoryUserRepository

repo = InMemoryUserRepository()
service = UserService(repo)

app = FastAPI()

@app.get("/get_users")
def get_users():
    return service.get_all_users()

@app.get("/get_user/{id}")
def get_user_by_id(id: int):
    user = service.get_user_by_id(id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return user

@app.post("/create_user")
def create_user(user_data: dict):
    return service.create_user(user_data)

@app.put("/update_user/{id}")
def update_user(id: int, user_data: dict):
    user = service.update_user(id, user_data)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return user

@app.delete("/delete_user/{id}")
def delete_user(id: int):
    user = service.delete_user(id)
    
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return {"detail": "user deleted"}

