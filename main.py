from fastapi import FastAPI, HTTPException
from service import UserService
from postgres_repository import PostgresUserRepository
from schemas import User, UserCreate, UserUpdate

repo = PostgresUserRepository()
service = UserService(repo)

app = FastAPI()

@app.get("/get_users", response_model=list[User])
def get_users():
    return service.get_all_users()

@app.get("/get_user/{id}", response_model=User)
def get_user_by_id(id: int):
    user = service.get_user_by_id(id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return user

@app.post("/create_user", response_model=User, status_code=201)
def create_user(user_data: UserCreate):
    return service.create_user(user_data.model_dump())

@app.put("/update_user/{id}", response_model=User)
def update_user(id: int, user_data: UserUpdate):
    user = service.update_user(id, user_data.model_dump(exclude_unset=True))
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return user

@app.delete("/delete_user/{id}")
def delete_user(id: int):
    user = service.delete_user(id)
    
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return {"detail": "user deleted"}

