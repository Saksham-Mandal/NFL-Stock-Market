import requests
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "nfl.db"

def fillDB():

    conn = sqlite3.connect(DB_PATH)

    try:
        cur = conn.cursor()

        cur.execute("SELECT id FROM teams")
        teamids = [row[0] for row in cur.fetchall()]
        
        count = 0
        for teamid in teamids:
            getFullRoster(teamid, conn)
            count += 1
            print(f"Team {count}/32 Completed")
        conn.commit()
    finally:
        conn.close()
    
    print(f"✅ DB filled")

def getFullRoster(teamnum: int, conn):
    
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

    try:
        cur = conn.cursor()

        data = response.json() # the make-up of data can be found in the Google Doc

        group = data["athletes"]
        for item in group:
            playerlist = item.get("items", [])
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
    except Exception as e:
        print(f"Error on team {teamnum}: {e}")
        raise

def fillTeamDB():
    print("Starting TeamDB Population...")
    getTeamInfo()
    print("TeamDB filled ✅")

def getTeamInfo():

    TEAM_URL = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams"

    response = requests.get(TEAM_URL, timeout=15)
    response.raise_for_status()

    sql = """
        INSERT INTO teams (
        id, full_team_name, team_location, 
        team_nickname, team_abbrev, team_logo, 
        team_prim_color, team_alt_color
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(id) DO UPDATE SET
            full_team_name   = excluded.full_team_name,
            team_location    = excluded.team_location,
            team_nickname    = excluded.team_nickname,
            team_abbrev      = excluded.team_abbrev,
            team_logo        = excluded.team_logo,
            team_prim_color  = excluded.team_prim_color,
            team_alt_color   = excluded.team_alt_color,
            updated_at       = CURRENT_TIMESTAMP
    """

    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        data = response.json()

        teams = data["sports"][0]["leagues"][0]["teams"] #this is the path to the list of NFL teams (called team in the diagram)

        for team in teams:
            teaminfo = team["team"]
            teamid = int(teaminfo["id"])
            abbreviation = teaminfo["abbreviation"]
            displayName = teaminfo["displayName"]
            nickname = teaminfo["nickname"]
            location = teaminfo["location"]
            color = "#" + teaminfo["color"]
            alternateColor = "#" + teaminfo["alternateColor"]
            #logo = teaminfo["logos"][0]["href"]
            logos = teaminfo.get("logos", [])
            logo = logos[0]["href"] if logos else None

            cur.execute(
                sql,
                (
                    teamid,
                    displayName,
                    location,
                    nickname,
                    abbreviation,
                    logo,
                    color,
                    alternateColor,
                ),
            )
        conn.commit()
    finally:
        conn.close()
    

def inspectEndpoint():
    print("Start of Inspection Code")
    #---------Endpoint Inspection Code---------#

    TEAM_URL = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams"
    
    response = requests.get(TEAM_URL, timeout=15)
    response.raise_for_status()

    data = response.json()

    #print("Inspecting data:")
    #print(type(data))
    #print(len(data))
    #print(data.keys())

    #print("Inspecting sports:")
    sports = data["sports"]
    #print(type(sports))
    #print(len(sports))

    #print("Inspecting item1")
    item1 = sports[0]
    #print(type(item1))
    #print(len(item1))
    #print(item1.keys())

    print("Inspecting leagues:")
    leagues = item1["leagues"]
    print(type(leagues))
    print(len(leagues))

    #print("Inspecting league1:")
    league1 = leagues[0]
    #print(type(league1))
    #print(len(league1))
    #print(league1.keys())

    #print("Inspecting teams:")
    teams = league1["teams"]
    #print(type(teams))
    #print(len(teams))

    print("Inspecting teams0:")
    teams0 = teams[0]
    print(type(teams0))
    print(len(teams0))
    print(teams0.keys())

    #print("Inspecting team:")
    team1 = teams0["team"]
    #print(type(team1))
    #print(len(team1))
    #print(team1.keys())

    #print("Inspecting abbreviation")
    #abbrev = team1["abbreviation"]
    #print(type(abbrev))
    #print(len(abbrev))
    #print(abbrev)

    #print("Inspecting logos:")
    logos = team1["logos"]
    #print(type(logos))
    #print(len(logos))

    logo1 = logos[0]
    #print(type(logo1))
    #print(len(logo1))
    #print(logo1.keys())
    #print(logo1["href"])

    #print(type(logo1["alt"]))
    #print(logo1["rel"])

    #for logo in logos:
    #    #print(logo.keys())
    #    print(logo["href"])

    #for nflteam in teams:
    #    currnum = nflteam["team"]["id"]
    #    currteam = nflteam["team"]["displayName"]
    #    primcolor = nflteam["team"]["color"]
    #    altcolor = nflteam["team"]["alternateColor"]
    #    print(f"ID {currnum}: {currteam}")
    #    print(f"Primary Color: {primcolor}")
    #    print(f"Alternate Color: {altcolor}")

    #--------------------------------#
    print("End of Inspection Code")

if __name__ == "__main__":
    #fillTeamDB()
    fillDB()
    #inspectEndpoint()