import sqlite3


db = sqlite3.connect(":memory:")
session = db.cursor()

session.execute("""CREATE TABLE images(
                       label text,
                       image_path text)""")
db.commit()

session.execute("INSERT INTO images VALUES (:label, :image_path)", {"label": "dog", "image_path": "dog/dog.jpg"})

def upload(label):
    session.execute("INSERT INTO images VALUES (:label, :image_path)", {"label": label, "image_path": "path"})
    db.commit()

def get(id):
    session.execute(f"SELECT * FROM images WHERE rowid == {id}")
    local_path = session.fetchone()[1]
    return local_path