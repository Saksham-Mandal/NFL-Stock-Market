import nflreadpy as nfl
import polars as pl

df = nfl.load_player_stats(seasons=[2024, 2025])

print(df.shape)
print(df.select(["season"]).unique())

player_df = df.filter(pl.col("player_display_name") == "Josh Allen")

print(player_df.select(["season", "week", "fantasy_points"]).sort(["season", "week"]))

rosters_df = nfl.load_rosters(seasons=[2026])

#print(rosters_df.columns)
#print(rosters_df.head())

#player_df = (
#    df.filter(pl.col("player_display_name") == "Kyle Pitts")
#      .select([
#          "player_display_name",
#          "season",
#         "week",
#          "season_type",
#          "team",
#          "opponent_team",
#          "completions",
#          "attempts",
#          "passing_yards",
#          "passing_tds",
#          "passing_interceptions",
#          "carries",
#          "rushing_yards",
#          "rushing_tds",
#          "fantasy_points",
#          "fantasy_points_ppr"
#      ])
#)

#print(player_df)

