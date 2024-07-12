from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    password: str

@app.post("/submit_form/")
async def submit_form(user: User):
    return {"username": user.username, "password": user.password}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


