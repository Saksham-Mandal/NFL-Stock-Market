from typing import List
from Player import Player
from Stats import Stats
from Candle import Candle

# 17 weeks of data gives 13 candles
# x weeks of data = x - 4 candles
# x candles require x + 4 weeks of data
# If our charts are going to all be, lets say, 25 candles long, it will require the player's last 28 weeks of data
# This raises the question of how rookies can be traded---will they need to play a minimum of 4 weeks?
# This also raises the question of how we will represent players with less than 28 weeks but more than 4 weeks of data

# This function returns a list of 13 candles
def create_chart(player: Player) -> List[Candle]:
    candlelist: List[Candle] = []

    ptr = 0

    while ptr + 4 < len(player.get_stats()):
        cand = create_candle(player, ptr)
        candlelist.append(cand)
        ptr = ptr + 1
    
    return candlelist

def avg_4FP(num1: float, num2: float, num3: float, num4: float) -> float:
    return ((num1 + num2 + num3 + num4) / 4)

#5 weeks are required to create one candle
def create_candle(player: Player, idx: int) -> Candle:
    
    wkcurr = player.get_stats()[idx].calc_fpts()
    wk1ago = player.get_stats()[idx + 1].calc_fpts()
    wk2ago = player.get_stats()[idx + 2].calc_fpts()
    wk3ago = player.get_stats()[idx + 3].calc_fpts()
    wk4ago = player.get_stats()[idx + 4].calc_fpts()

    wick = wkcurr
    open = avg_4FP(wk1ago, wk2ago, wk3ago, wk4ago)
    close = avg_4FP(wkcurr, wk1ago, wk2ago, wk3ago)
    return Candle(open, close, wick)