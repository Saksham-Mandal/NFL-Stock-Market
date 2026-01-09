import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "nfl.db"


def clearDB():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM players;")


def deletePlayer(playerid: str):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM players WHERE id = ?;",
            (playerid,),
        )