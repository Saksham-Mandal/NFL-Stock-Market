from api import app
from db.espn_client import fillDB, fillTeamDB
from db.init_db import init_db
from db.clear_db import clearDB, clearTeamsDB

def main():
    command = input("""
    What do you want to do?
    [refresh (r)]: Refresh the database
    [init (i)]: Initialize the database
    [populate (p)]: Populate the database
    [clear (c)]: Clear the database
    [start (s)]: Start the backend server
    > """).lower().strip()

    if command == "refresh" or command == "r":
       print("Refreshing databases...")
       refresh_dbs()
       print("Databases refreshed ✅")
    elif command == "init" or command == "i":
        print("Initializing database...")
        init_db()
        print("Databases Initialized and Populated ✅")
    elif command == "populate" or command == "p":
        command = input("""
        What do you want to do?
        [teamplay (tp)]: Populate the teams & players tables
        [games (g)]: Populate the games table
        > """).lower().strip()

        if command == "teamplay" or command == "tp":
            print("Populating teams & players tables...")
            refresh_dbs()
            print("teams & players tables filled ✅")
        elif command == "games" or command == "g":
            print("Populating games table...")
    elif command == "clear" or command == "c":
        print("Clearing databases...")
        clear_dbs()
        print("Databases cleared ✅")
    elif command == "start" or command == "s":
        print("Starting backend server...")
        start_backend()
    else:
        print("Error: Invalid User Command")
    

def start_backend():
    app.run(port=5050, debug=True, use_reloader=False)

def refresh_dbs():
    fillTeamDB()
    fillDB()

def initp_dbs():
    #clear_dbs()
    print("Initializing...")
    init_db()
    print("Initialized ✅")
    print("Populating...")
    refresh_dbs()
    print("Populated ✅")

def clear_dbs():
    clearDB()
    clearTeamsDB()


if __name__ == "__main__":
    main()