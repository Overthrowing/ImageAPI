from fastapi import FastAPI
from fastapi.responses import FileResponse
from database import *
from os import path
app = FastAPI()


@app.get("/")
def read_root():
    return {"Message": "Welcome to ImageAPI"}

@app.get("/images/{id}")
async def get_image(id: int):
    local_path = get(id)
    path = f"images/{local_path}"
    print(path)
    return FileResponse(path)

@app.post("/image/")
async def post_image(label: str, format: str, image):
    upload(label)
    return {"result": "Positive"}



