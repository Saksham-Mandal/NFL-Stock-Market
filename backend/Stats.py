class Stats:

    def __init__(
            self, season, week, pos,
            pass_yds, pass_td,
            pass_int, pass_2pt, rush_yds,
            rush_td, rush_2pt, receptions,
            rec_yds, rec_td, rec_2pt,
            fumbles_lost, fumble_td,
            pass_epa, rec_epa, rush_epa,
            targs, targ_share, carries):
        
        #time/player info
        self.season = season
        self.week = week
        self.pos = pos

        #passing stats
        self.pass_yds = pass_yds
        self.pass_td = pass_td
        self.pass_int = pass_int
        self.pass_2pt = pass_2pt

        #rushing stats
        self.rush_yds = rush_yds
        self.rush_td = rush_td
        self.rush_2pt = rush_2pt

        #recieving stats
        self.receptions = receptions
        self.rec_yds = rec_yds
        self.rec_td = rec_td
        self.rec_2pt = rec_2pt

        #fumbles
        self.fumbles_lost = fumbles_lost
        self.fumble_td = fumble_td

        #advanced metrics
        self.pass_epa = pass_epa
        self.rec_epa = rec_epa
        self.rush_epa = rush_epa
        self.targs = targs
        self.targ_share = targ_share
        self.carries = carries
    
    def calc_FP(self):
        fantasy_points = 0

        # passing
        fantasy_points += self.pass_yds * 0.04
        fantasy_points += self.pass_td * 4
        fantasy_points -= self.pass_int * 2
        fantasy_points += self.pass_2pt * 2

        # rushing
        fantasy_points += self.rush_yds * 0.1
        fantasy_points += self.rush_td * 6
        fantasy_points += self.rush_2pt * 2

        # receiving
        fantasy_points += self.receptions * 1  # full PPR
        fantasy_points += self.rec_yds * 0.1
        fantasy_points += self.rec_td * 6
        fantasy_points += self.rec_2pt * 2

        # fumbles
        fantasy_points -= self.fumbles_lost * 2
        fantasy_points += self.fumble_td * 6

        return fantasy_points
