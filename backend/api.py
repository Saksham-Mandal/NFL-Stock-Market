from flask import Flask, request, jsonify
from pathlib import Path
from flask_cors import CORS
from candle_engine import generate_candles
import sqlite3

DB_PATH = Path(__file__).resolve().parent / "db" / "nfl.db"

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)
CORS(
    app,
    resources={r"/api/*": {"origins": [
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ]}}
)

#player endpoint---gets player information (except for player stats)
@app.get("/api/player")
def getPlayerInfo():
    name = (request.args.get("name") or "").strip()
    if not name:
        return jsonify({
            "found": False,
            "error": "Missing 'name' query parameter"
        }), 400

    conn = get_conn()
    row = conn.execute(
        """
        SELECT * FROM players WHERE LOWER(full_name) = LOWER(?) LIMIT 1;
        """,
        (name,)
    ).fetchone()
    conn.close()

    if row is None:
        return jsonify({"found": False}), 404
    
    return jsonify({"found": True, "player": dict(row)})

#suggestion endpoint---gets players with similar names (for searching)
@app.get("/api/suggest")
def suggestPlayers():
    q = (request.args.get("q") or "").strip()
    
    if len(q) < 2:
        return jsonify({
            "q": q,
            "results": []
        })

    conn = get_conn()
    rows = conn.execute(
        """
        SELECT id, full_name FROM players
        WHERE LOWER(full_name) LIKE '%' || LOWER(?) || '%'
        LIMIT 10;
        """, (q,)
    ).fetchall()
    conn.close()

    return jsonify({
        "q": q,
        "results": [dict(r) for r in rows]
    })

#team endpoint---gets needed team information
@app.get("/api/team")
def get_team_info():
    team_id = request.args.get("team_id", type=int)

    if team_id is None:
        return jsonify({"found": False, "error": "team_id is required"}), 400

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute("SELECT * FROM teams WHERE id = ?", (team_id,))
    row = cur.fetchone()
    conn.close()

    if row is None:
        return jsonify({"found": False, "error": "Team not found"}), 404

    return jsonify({
        "found": True,
        "team": dict(row)
    })

#stats endpoint---gets stats for a given player
@app.get("/api/stats")
def get_candle_chart():
    nflverse_id = (request.args.get("nflverse_id") or "").strip()

    if not nflverse_id:
        return jsonify({"found": False, "error": "nflverse_id is required"}), 400
    
    candles = generate_candles(nflverse_id)

    return jsonify({
        "found": True,
        "nflverse_id": nflverse_id,
        "candles": candles
    })

if __name__ == "__main__":
    app.run(port=5000, debug=True)