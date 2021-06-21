import base64
import os


def to_png(location, img_data):
    with open(location, "wb") as file:
        file.write(base64.b64decode(img_data))

def delete_image(path):
    if os.path.exists(path):
        os.remove(path)

def generate_pallet():
    pass
