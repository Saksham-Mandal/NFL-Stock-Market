class Candle:
    def __init__(self, open: float, close: float, wick: float):
        self.open = open
        self.close = close
        self.wick = wick

    def get_open(self) -> float:
        return self.open
    
    def get_close(self) -> float:
        return self.close
    
    def get_wick(self) -> float:
        return self.wick