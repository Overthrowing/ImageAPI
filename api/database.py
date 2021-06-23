import os
import sqlite3

DATABASE_NAME = "database.db"

if not os.path.exists(DATABASE_NAME):
    db = sqlite3.connect(DATABASE_NAME)
    session = db.cursor()
    session.execute(
        """CREATE TABLE images(
                label text,
                image_path text
            )
    """
    )
    db.commit()

db = sqlite3.connect(DATABASE_NAME)
session = db.cursor()


def upload(label, path):
    session.execute(
        "INSERT INTO images VALUES (:label, :path)", {"label": label, "path": path}
    )
    db.commit()


def get_image_by_id(id):
    session.execute("SELECT image_path, * FROM images WHERE rowid=?", (id,))
    path = session.fetchone()
    if path:
        path = path[0]
        return path
    else:
        return None


def get_images_by_label(img_label):
    session.execute("SELECT image_path, * FROM images WHERE label=?", (img_label,))
    images = session.fetchall()
    return images


def get_image_id(img_label, id):
    session.execute("SELECT rowid, * FROM images WHERE label=?", (img_label,))
    images = session.fetchall()
    if images:
        return images[id][0]
    else:
        return None


def delete_image_by_id(id):
    session.execute("DELETE FROM images WHERE rowid=?", (id,))
    db.commit()


def delete_category(img_label):
    session.execute("DELETE FROM images WHERE label=?", (img_label,))
    db.commit()
