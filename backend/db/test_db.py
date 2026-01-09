import sqlite3

conn = sqlite3.connect("db/nfl.db")
cur = conn.cursor()

cur.execute("""
INSERT INTO players (id, full_name, position, team_id, active)
VALUES (?, ?, ?, ?, ?)
""", (
    "TEST_PLAYER",
    "Test Player",
    "QB",
    "TEST",
    1
))

conn.commit()

cur.execute(
    "SELECT * FROM players WHERE id = ?",
    ("TEST_PLAYER",)
)

row = cur.fetchone()
print(row)

cur.execute(
    "DELETE FROM players WHERE id = ?",
    ("TEST_PLAYER",)
)
conn.commit()
conn.close()
