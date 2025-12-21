def daylight_hours(latitude):
    daylight_latitude = {
        '-90': 24,
        '-75': 23,
        '-60': 21,
        '-45': 15,
        '-30': 13,
        '-15': 12,
        '0': 12,
        '15': 11,
        '30':10,
        '45':9,
        '60': 6,
        '75': 2,
        '90': 0
    }
    keys = list(daylight_latitude.keys())
    l = 0 
    r = len(keys) - 1
    while l <= r:
        m = (l + r)//2
        if int(keys[m]) == latitude:
            return daylight_latitude[keys[m]]
        elif latitude < int(keys[m]):
            r = m - 1
        else:
            l = m + 1
    if r > 0:
        return daylight_latitude[keys[l]]
    else:
        return daylight_latitude[keys[r]]