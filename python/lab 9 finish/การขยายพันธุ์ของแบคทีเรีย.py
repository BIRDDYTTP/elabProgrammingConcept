def nb_year(p0,percent,aug,p):
    day = 0
    while p0 < p:
        ans = p0 + (p0 * (percent/100)) + aug
        p0 = int(ans)
        day += 1
    return day