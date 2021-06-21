import sqlite3
from utils import delete_image

db = sqlite3.connect(":memory:")
session = db.cursor()

session.execute("""CREATE TABLE images(
                       label text,
                       image_path text)""")
db.commit()

def upload(label, path):
    session.execute("INSERT INTO images VALUES (:label, :path)", {"label": label, "path": path})
    db.commit()


def get_image_by_id(id):
    session.execute("SELECT * FROM images WHERE rowid=?", (id,))
    path = session.fetchone()[1]
    return path


def get_images_by_label(img_label):
    session.execute("SELECT * FROM images WHERE label=?", (img_label,))
    images = session.fetchall()
    return images

def delete_image_by_id(id):
    session.execute("DELETE * FROM images WHERE rowid=?", (id,))
