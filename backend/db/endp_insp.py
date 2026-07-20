import requests

def inspect_sched_endp():
    URL = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard?dates=2026&seasontype=2&week=1"

    response = requests.get(URL, timeout=15)
    response.raise_for_status()

    data = response.json()

    print(type(data))
    print(len(data))
    print(data.keys())

if __name__ == "__main__":
    inspect_sched_endp()