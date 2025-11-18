class Stats:

    def __init__(self, yards: int, TDs: int):
        self.yards = yards
        self.TDs = TDs

    def calc_fpts(self) -> float:
        TDpts: float = (self.TDs * 6)
        yardpts: float = (self.yards * 0.1)
        totalpts: float = TDpts + yardpts
        return totalpts
    
    def get_yards(self) -> float:
        return self.yards
    
    def get_TDs(self) -> float:
        return self.TDs