from fastapi import FastAPI, HTTPException

app = FastAPI()

user_data = {
"user1": {"id": 111, "name": "Alice", "age": 30, "email": "alice@gmail.com"},
"user2": {"id": 222, "name": "Bob", "age": 25, "email": "bob@gmail.com"},
"user3": {"id": 333, "name": "Charlie", "age": 35, "email": "charlie@gmail.com"}
}    

@app.get("/get_users")
def get_users():
    if not user_data:
        raise HTTPException(status_code=404, detail="no users found")
    return user_data

@app.get("/get_user/{id}")
def get_user_by_id(id: int):
    for user in user_data.values():
        if user["id"] == id:
            return user
    raise HTTPException(status_code=404, detail="user not found")


