import nflreadpy as nfl
import polars as pl
from datetime import datetime

_stats_df = None

def get_stats_season():
    today = datetime.now()
    season_start = datetime(today.year, 9, 1)
    if today >= season_start:
        return today.year
    else:
        return today.year - 1

def load_stats():
    global _stats_df
    if _stats_df is None:
        stats_season = get_stats_season()
        seasons = list(range(stats_season - 9, stats_season + 1))
        _stats_df = nfl.load_player_stats(seasons=seasons)
    return _stats_df

def get_player_stats_df(nflverse_player_id: str):
    df = load_stats()
    return (
        df
        .filter(pl.col("player_id") == nflverse_player_id)
        .select([
            # time info
            "season",
            "week",
            # player info
            "position",
            
            # <-----Fantasy Point Info---->
            # QB info
            "passing_yards",
            "passing_2pt_conversions",
            "passing_interceptions",
            # rushing info
            "rushing_yards",
            "rushing_2pt_conversions",
            # receiving info
            "receiving_yards",
            "receptions",
            "receiving_2pt_conversions",
            # TD info
            "receiving_tds",
            "rushing_tds",
            "passing_tds",
            "fumble_recovery_tds",
            # other
            "sack_fumbles_lost",
            "rushing_fumbles_lost",
            "receiving_fumbles_lost",
            # <------------------------>
            
            # advanced metrics
            "passing_epa",
            "rushing_epa",
            "receiving_epa",
            "targets",
            "target_share",
            "carries",
        ])
        .sort(["season", "week"])
        )