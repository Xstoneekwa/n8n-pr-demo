from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/users")
def get_users():
    return {"users": ["Alice", "Bob"]}
@app.get("/admin/data")
def admin_data():
    return {"password": "123456", "token": "abc123"}

@app.get("/admin/data/v1")
def admin_data_v1():
    return {"password": "123456", "token": "abc123"}
