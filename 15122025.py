def speed_check(speed_mph, speed_limit_kph):
    mile_to_km = 1.60934
    speed_in_km = speed_mph * mile_to_km
    if speed_in_km <= speed_limit_kph:
        return "Not Speeding"
    elif speed_in_km > speed_limit_kph and speed_in_km <= (speed_limit_kph + 5):
        return "Warning"
    else:
        return "Ticket"