import requests
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "nfl.db"

def fillDB():
    for i in range(1, 32, 1):
        getFullRoster(i)

def getFullRoster(teamnum: int):
    
    ROSTER_URL = f"https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams/{teamnum}/roster"
    
    response = requests.get(ROSTER_URL, timeout=15)
    response.raise_for_status()

    sql = """
    INSERT INTO players (
        id, full_name, first_name, last_name,
        position, team_id, active,
        height_in, weight_lb, age,
        date_of_birth, headshot_url
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ON CONFLICT(id) DO UPDATE SET
        full_name     = excluded.full_name,
        first_name    = excluded.first_name,
        last_name     = excluded.last_name,
        position      = excluded.position,
        team_id       = excluded.team_id,
        active        = excluded.active,
        height_in     = excluded.height_in,
        weight_lb     = excluded.weight_lb,
        age           = excluded.age,
        date_of_birth = excluded.date_of_birth,
        headshot_url  = excluded.headshot_url,
        updated_at    = CURRENT_TIMESTAMP
    """

    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()

        data = response.json() # the make-up of data can be found in the Google Doc

        group = data["athletes"]
        for item in group:
            if item["position"] == "offense":
                playerlist = item["items"]
                for player in playerlist:
                    pos = (player.get("position") or {}).get("abbreviation")
                    if pos in {"QB", "RB", "WR", "TE"}:
                        player_id = player.get("id")
                        full_name = player.get("fullName")
                        first_name = player.get("firstName")
                        last_name = player.get("lastName")

                        # Roster endpoint represents roster membership; treat stored row as active.
                        active = 1

                        height_in = player.get("height")
                        weight_lb = player.get("weight")
                        age = player.get("age")
                        dob = player.get("dateOfBirth")

                        headshot_dict = player.get("headshot") or {}
                        headshot_url = headshot_dict.get("href")

                        # Skip if essential fields are missing
                        if not player_id or not full_name or not pos:
                            continue

                        cur.execute(
                            sql,
                            (
                                player_id,
                                full_name,
                                first_name,
                                last_name,
                                pos,
                                teamnum,
                                active,
                                height_in,
                                weight_lb,
                                age,
                                dob,
                                headshot_url,
                            ),
                        )
        conn.commit()
    finally:
        conn.close()



    #---------Inspection Code---------#
    #print("Start of Inspection Code")

    #print("Inspecting data:")
    #print(type(data))
    #print(len(data))
    #print(data.keys())

    #print("Inspecting team")
    #team = data["team"]
    #print(type(team))
    #print(len(team))
    #print(team.keys())
    
    #print("Inspecting id")
    #id = team["id"]
    #print(type(id))
    #print(id)

    #print("Inspecting athletes:")
    #athletes = data["athletes"]
    #print(type(athletes))
    #print(len(athletes))

    #print("Inspecting item1:")
    #item1 = athletes[0]
    #print(type(item1))
    #print(len(item1))
    #print(item1.keys())

    #print("Inspecting position:")
    #pos = item1["position"]
    #print(type(pos))
    #print(pos)

    #for athlete in athletes:
        #print(athlete["position"])


    #print("Inspecting items (inside item1):")
    #items = item1["items"]
    #print(type(items))
    #print(len(items))

    #print("Inspecting player1 (inside items)")
    #player1 = items[0]
    #print(type(player1))
    #print(len(player1))
    #print(player1.keys())

    #print("Inspecting Headshot")
    #headshot223 = player1["headshot"]
    #print(player1["fullName"])
    #print(type(headshot223))
    #print(headshot223.keys())
    #print(type(headshot223["href"]))
    #print(type(headshot223["alt"]))
    #print(headshot223["href"]) #headshot link
    #print(headshot223["alt"])
    
    #print("Inspecting Status:")
    #status = player1["status"]
    #print(type(status))
    #print(status.keys())
    #print(status["id"])
    #print(status["name"])
    #print(status["type"])
    #print(status["abbreviation"])

    #group = data["athletes"]

    #count = 0
    #for item in group:
    #    if item["position"] == "offense":
    #        playerlist = item["items"]
    #        for player in playerlist:
    #            if player["position"]["abbreviation"] in {"QB", "WR", "RB", "TE"}:
    #                print(player["id"])
    #                print(player["fullName"])
    #                print(player["firstName"])
    #                print(player["lastName"])
    #                print(player["position"]["abbreviation"])
    #                print(teamID)
    #                print(player["status"]["id"])
    #                print(player["status"]["type"])
    #                print(player["height"])
    #                print(player["weight"])
    #                print(player["age"])
    #                print(player["dateOfBirth"])
    #                count = count + 1
    #            else: continue
    #    else: continue
    
    #print("Number of Players: " + str(count))

    #print("End of Inspection Code")
    #--------------------------------#