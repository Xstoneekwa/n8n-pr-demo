from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/users")
def get_users():
    return {"users": ["Alice", "Bob"]}
@app.get("/users/v1")
def get_users_v1():
    return {"users": ["Alice", "Bob"], "version": "v1"}
    @app.get("/messages")
def messages():
    return {"message": "ok"}

@app.get("/messages/v1")
def messages_v1():
    return {"message": "ok"}
