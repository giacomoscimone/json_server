from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/login/")
async def login(request: Request):
    data = await request.json()
    username = data.get("username")
    password = data.get("password")
    if username is not None and password is not None:
        login_result = "success"
    else:
        login_result = "failure"
    return {"username": username, "login": login_result }
