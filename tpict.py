import sqlite3 as sq

db = sq.connect("person.db")
cur = db.cursor()

# async def get_photo(name):
#      return (cur.execute(f"SELECT id FROM images where name =='{name}'").fetchone()[0])

name = "pic"
id = "AgACAgIAAxkBAAICOGZtfZ4wj_ByIySz4fR7z4ejQIlpAAJG2DEbTHRoSxnU6kg_O0anAQADAgADeAADNQQ"

cur.execute("INSERT INTO images VALUES (?, ?)", (name, id))
db.commit()