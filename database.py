import sqlite3
import os

DATABASE_NAME = "database.db"

db = sqlite3.connect(DATABASE_NAME)
session = db.cursor()

if not os.path.exists(DATABASE_NAME):
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
    db.commit()

def delete_category(img_label):
    session.execute("DELETE * FROM images WHERE label=?", (img_label,))
    db.commit()
