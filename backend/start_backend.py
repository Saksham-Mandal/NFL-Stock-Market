from api import app
from db.espn_client import fillDB, fillTeamDB
from db.init_db import init_db
from db.clear_db import clearDB, clearTeamsDB

def main():
    command = input("""
    What do you want to do?
    [refresh (r)]: Refresh the databases
    [init (i)]: Initialize and Populate the databases
    [clear (c)]: Clear the databases
    [start (s)]: Start the backend server
    > """).lower().strip()

    if command == "refresh" or command == "r":
       print("Refreshing databases...")
       refresh_dbs()
       print("Databases refreshed ✅")
    elif command == "init" or command == "i":
        print("Initializing/Populating databases...")
        initp_dbs()
        print("Databases Initialized and Populated ✅")
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
    app.run(port=5000, debug=True, use_reloader=False)

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