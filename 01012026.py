def resolution_streak(days):
    for index,(walk,screen_time,pages) in enumerate(days):
        if not(walk >= 10000 and screen_time <= 120 and pages >= 5):
           return f"Resolution failed on day {index+1}: {index} day streak." 
    return f"Resolution on track: {len(days)} day streak."
