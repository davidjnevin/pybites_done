from fastapi import FastAPI

MSG = "Welcome to PyBites' FastAPI Learning Path 🐍 🎉"

app = FastAPI()


@app.get("/")
async def root():
    return {"message": MSG}
