from Stats import Stats

class Player:
    def __init__(self, name: str, team: str, pos: str, stats: list[Stats]):
        self.name = name
        self.team = team
        self.pos = pos
        self.stats = stats

    def get_name(self) -> str:
        return self.name
    
    def get_team(self) -> str:
        return self.team
    
    def get_pos(self) -> str:
        return self.pos
    
    def get_stats(self) -> list[Stats]:
        return self.stats