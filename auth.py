import sqlite3

conn = sqlite3.connect(
    "database/users.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(

id INTEGER PRIMARY KEY AUTOINCREMENT,

name TEXT,

email TEXT UNIQUE,

password TEXT

)
""")

conn.commit()


def register_user(
        name,
        email,
        password
):

    try:

        cursor.execute(
            """
            INSERT INTO users
            (name,email,password)

            VALUES(?,?,?)
            """,
            (
                name,
                email,
                password
            )
        )

        conn.commit()

        return True

    except:

        return False


def login_user(
        email,
        password
):

    cursor.execute(
        """
        SELECT * FROM users

        WHERE email=?

        AND password=?
        """,
        (
            email,
            password
        )
    )

    user = cursor.fetchone()

    return user