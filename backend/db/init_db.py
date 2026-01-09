import sqlite3
from pathlib import Path

# To Initialize Database (delete old one first): python3 backend/db/init_db.py

DB_PATH = Path(__file__).resolve().parent / "nfl.db"
SCHEMA_PATH = Path(__file__).resolve().parent / "schema.sql"

def init_db():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    try:
        conn.execute("PRAGMA foreign_keys = ON;")
        schema = SCHEMA_PATH.read_text(encoding="utf-8")
        conn.executescript(schema)
        conn.commit()
        print(f"✅ DB initialized at: {DB_PATH}")
    finally:
        conn.close()

if __name__ == "__main__":
    init_db()