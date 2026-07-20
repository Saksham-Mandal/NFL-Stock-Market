import sqlite3
from passwords import hash_password, check_password

def create_user(conn, username: str, email: str, password: str):
    password_hash = hash_password(password)

    try:
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO users (username, email, password_hash)
            VALUES (?, ?, ?)
            """,
            (username, email, password_hash)
        )

        conn.commit()

        return {
            "success": True,
            "user_id": cursor.lastrowid
        }

    except sqlite3.IntegrityError:
        return {
            "success": False,
            "error": "Username or email already exists"
        }

def get_user_by_email(conn, email: str):
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, username, email, password_hash
        FROM users
        WHERE LOWER(email) = LOWER(?)
        LIMIT 1
        """,
        (email,)
    )

    return cursor.fetchone()


def verify_user_login(conn, email: str, password: str):
    user = get_user_by_email(conn, email)

    if user is None:
        return None

    stored_hash = user["password_hash"]

    if not check_password(password, stored_hash):
        return None

    return {
        "id": user["id"],
        "username": user["username"],
        "email": user["email"]
    }
