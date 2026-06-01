from Stats import Stats

sclfactor = 3

def get_HL(weekstats: Stats):
    HL = weekstats.calc_FP()
    return HL

def get_score(playerstats: list[Stats], candlenum: int):
    if candlenum < 2:
        return None

    fp_0 = playerstats[candlenum].calc_FP()
    fp_1 = playerstats[candlenum - 1].calc_FP()
    fp_2 = playerstats[candlenum - 2].calc_FP()


    production = (fp_0 + fp_1 + fp_2) / 3

    if candlenum < 5:
        trend = 0
    else:
        fp_3 = playerstats[candlenum - 3].calc_FP()
        fp_4 = playerstats[candlenum - 4].calc_FP()
        fp_5 = playerstats[candlenum - 5].calc_FP()

        trend = production - ((fp_3 + fp_4 + fp_5) / 3)
    
    mean = production
    variance = ((fp_0 - mean) ** 2 + (fp_1 - mean) ** 2 + (fp_2 - mean) ** 2) / 3
    std_dev = variance ** 0.5
    consistency = -(std_dev)

    score = 0.65 * production + 0.10 * trend + 0.25 * consistency

    return score

def get_close(playerstats: list[Stats], candlenum: int, prev_close: float):
    curr_score = get_score(playerstats, candlenum)
    prev_score = get_score(playerstats, (candlenum - 1))

    if prev_score is None:
        prev_score = curr_score

    delta = curr_score - prev_score

    close_price = prev_close + (delta * sclfactor)
    return close_price