from player_statistics import get_player_stats_df
from formula import get_HL, get_close
from Stats import Stats
from datetime import datetime, timedelta

candle_cache: list[dict] = []
playerstats: list[Stats] = []

def generate_candles(nflverseid: str):
    candle_cache.clear()
    playerstats.clear()
    stats_df = get_player_stats_df(nflverseid)
    games = stats_df.to_dicts()
    insert_stats(games, playerstats)
    for i in range(len(playerstats)):
        weekstats = playerstats[i]
        
        if i < 2: #not enough info---no candle generated
            continue
        
        HL = get_HL(weekstats)

        if i == 2: #first candle generated (candle 0)
            base_price = (
                (playerstats[0].calc_FP() +
                playerstats[1].calc_FP() +
                playerstats[2].calc_FP()) / 3
                )

            if (HL > base_price):
                high = HL
                low = base_price
            elif (HL < base_price):
                low = HL
                high = base_price
            else:
                high = base_price
                low = base_price

            candle = {
                "time": get_time(weekstats.season, weekstats.week),
                "open": base_price,
                "high": high,
                "low": low,
                "close": base_price
            }

            candle_cache.append(candle)
            continue

        #every other candle generated (candles 3 and 4 won't have the trend calculation)

        open_price = candle_cache[-1]["close"]
        close_price = get_close(playerstats, i, open_price)
        
        high = max(open_price, close_price, HL)
        low = min(open_price, close_price, HL)
        
        candle = {
            "time": get_time(weekstats.season, weekstats.week),
            "open": open_price,
            "high": high,
            "low": low,
            "close": close_price
        }

        candle_cache.append(candle)
    return candle_cache

def insert_stats(games: list[dict], playerstats: list[Stats]):
    for game in games:
        stats = Stats(
            season=to_int(game.get("season")),
            week=to_int(game.get("week")),
            pos=game.get("position"),

            pass_yds=to_int(game.get("passing_yards")),
            pass_td=to_int(game.get("passing_tds")),
            pass_int=to_int(game.get("passing_interceptions")),
            pass_2pt=to_int(game.get("passing_2pt_conversions")),

            rush_yds=to_int(game.get("rushing_yards")),
            rush_td=to_int(game.get("rushing_tds")),
            rush_2pt=to_int(game.get("rushing_2pt_conversions")),

            receptions=to_int(game.get("receptions")),
            rec_yds=to_int(game.get("receiving_yards")),
            rec_td=to_int(game.get("receiving_tds")),
            rec_2pt=to_int(game.get("receiving_2pt_conversions")),

            fumbles_lost=(
                to_int(game.get("sack_fumbles_lost")) +
                to_int(game.get("rushing_fumbles_lost")) +
                to_int(game.get("receiving_fumbles_lost"))
            ),

            fumble_td=to_int(game.get("fumble_tds")),

            pass_epa=float(game.get("passing_epa", 0) or 0),
            rec_epa=float(game.get("receiving_epa", 0) or 0),
            rush_epa=float(game.get("rushing_epa", 0) or 0),

            targs=to_int(game.get("targets")),
            targ_share=float(game.get("target_share", 0) or 0),
            carries=to_int(game.get("carries"))
        )

        playerstats.append(stats)

def to_int(value):
    try:
        return int(float(value))  # handles "12" and "12.0"
    except (TypeError, ValueError):
        return 0

def get_time(season: any, week: any):
    start_date = datetime(season, 9, 13)

    game_date = start_date + timedelta(days=(week - 1) * 7)

    return game_date.strftime("%Y-%m-%d")

if __name__ == "__main__":
    generate_candles("00-0037263")
