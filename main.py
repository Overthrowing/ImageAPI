from fastapi import FastAPI
from fastapi.responses import FileResponse

from database import *
from utils import *

app = FastAPI()


@app.get("/")
def read_root():
    return {"Message": "Welcome to ImageAPI"}


@app.get("/image/{id}")
async def get_image(id: int):
    path = get_image_by_id(id)
    return FileResponse(path)


@app.get("/images/{label}/{id}")
async def get_image_by_label(label: str, id: int):
    images = get_images_by_label(label)
    path = images[id][1]
    return FileResponse(path)


@app.post("/image/{label}/")
async def post_image(label: str, image: str):
    name = label + str(len(get_images_by_label(label)))
    path = f"images/{name}.png"
    to_png(path, image)
    upload(label, path)
    return {"result": "Success"}


@app.delete("/image/{id}")
async def get_image(id: int):
    path = get_image_by_id(id)
    delete_image(path)
    delete_image_by_id(id)
