from Player import Player
from parser import loadPlayers
from Chart import create_chart

def main():
    players = loadPlayers("data2.txt")
    for p in players:
        
        print(p.name)
        candlelist = create_chart(p)

        reversed_candles = list(reversed(candlelist))
        
        for idx, candle in enumerate(reversed_candles, start=1):
            print("Candle #" + str(idx))
            print("Open: " + str(candle.get_open()))
            print("Close: " + str(candle.get_close()))
            print("Wick: " + str(candle.get_wick()))
            print()

def getCurrPrice():
    print("price")

if __name__ == "__main__":
    main()