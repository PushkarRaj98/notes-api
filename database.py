import sqlite3


conn = sqlite3.connect("notes.db", check_same_thread=False)

cursor = conn.cursor()

# create table

cursor.execute("""
CREATE TABLE IF NOT EXISTS notes (
id INTEGER PRIMARY KEY AUTOINCREMENT,
text TEXT
)
""")

conn.commit()
