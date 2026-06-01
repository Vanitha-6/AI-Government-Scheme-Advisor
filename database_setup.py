import sqlite3

conn = sqlite3.connect("database/users.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    email TEXT UNIQUE,
    password TEXT
)
""")

conn.commit()
conn.close()

print("Database Created Successfully!")