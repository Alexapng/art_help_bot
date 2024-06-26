import sqlite3 as sq

db = sq.connect("/Users/aleksandra/PycharmProjects/pythonProject5/person1.db")
cur = db.cursor()

async def start_db():
    global db, cur
    cur.execute("CREATE TABLE IF NOT EXISTS person(user_id TEXT PRIMARY KEY, name TEXT, age TEXT, mail TEXT)")
    db.commit()

async def check_profile(user_id):
    user = cur.execute(f"SELECT 1 FROM person where user_id == {user_id}").fetchone()
    if not user:
        return False
    return True

async def create_profile(user_id):
    user = cur.execute(f"SELECT 1 FROM person where user_id == {user_id}").fetchone()
    if not user:
        cur.execute("INSERT INTO person VALUES(?, ?, ?, ?)", (user_id, '', '', ''))
        db.commit()

async def edit_profile(id, name, age, mail):
    cur.execute(f"UPDATE person SET name = ?, age = ?, mail = ? WHERE user_id == ?", (name, age, mail, id))
    db.commit()

# cur.execute("CREATE TABLE IF NOT EXISTS person(user_id TEXT PRIMARY KEY, name TEXT, age TEXT, mail TEXT)")
# cur.execute("INSERT INTO person VALUES(?, ?, ?, ?)", (id, name, age, mail))
# db.commit()
# cur.execute(f"UPDATE person SET name = ?, age = ?, mail = ? WHERE user_id == ?", (name, age, mail, id))
# db.commit()