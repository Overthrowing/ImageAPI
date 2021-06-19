from fastapi import FastAPI
from fastapi.responses import FileResponse
from database import *
from utils import *
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

@app.get("/images/{label}/{id}")
async def get_image(label: str, id: int):
    local_path = get(id)
    path = f"images/{local_path}"
    return FileResponse(path)

@app.post("/imagee/{label}/")
async def post_image(label: str, image: str):
    path = f"images/{label}/dog.png"
    print(path)
    to_png(path, image)
    upload(label, f"{label}/dog.png")
    return {"result": "Positive"}

