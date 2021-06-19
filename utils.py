import base64

def to_png(location, img_data):
    #location += ".png"
    with open(location, "wb") as file:
        file.write(base64.b64decode(img_data))
        
def generate_pallet():
    pass