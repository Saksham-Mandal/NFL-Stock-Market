from typing import List
from Player import Player
from Stats import Stats

def loadPlayers(path: str) -> List[Player]:
    players: List[Player] = []

    with open(path, "r") as f:
        data = f.readlines() #puts all lines from input file into variable data (List of strings)

    i = 0
    num_players = int(data[i].strip())
    i += 1

    for _ in range(num_players):

        # Read player metadata
        name = data[i].strip()
        team = data[i + 1].strip()
        pos = data[i + 2].strip()
        i += 3

        weekly_stats: list[Stats] = []

        # Read 17 weeks of stats
        for _ in range(17):
            line = data[i].strip()
            i += 1

            parts = line.split() #storing line as an array of strings--["Week#", "TDs", "Yards"]

            yards = int(parts[1])
            tds = int(parts[2])

            weekly_stats.append(Stats(yards, tds))

        players.append(Player(name, team, pos, weekly_stats))

    return players