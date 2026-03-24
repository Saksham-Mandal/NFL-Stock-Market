import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "nfl.db"


def clearDB():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM players;")
    print(f"✅ DB cleared")


def deletePlayer(playerid: str):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM players WHERE id = ?;",
            (playerid,),
        )

if __name__ == "__main__":
    clearDB()