import base64
import os
import colorific

def to_png(location, img_data):
    with open(location, "wb") as file:
        file.write(base64.b64decode(img_data))


def delete_image(path):
    if os.path.exists(path):
        os.remove(path)


def generate_pallet(image_path, max_colors):
    pallet = colorific.extract_colors(image_path, min_prominence=0.1, max_colors=max_colors)
    colors = [colorific.rgb_to_hex(c.value) for c in pallet.colors]
    if colors:
        return colors
    else:
        return None

