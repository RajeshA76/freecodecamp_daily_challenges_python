def compare_energy(calories_burned, watt_hours_used):
    CAL_JOULE = 4184
    WATT_JOULE = 3600

    if calories_burned * CAL_JOULE > watt_hours_used * WATT_JOULE:
        return "Workout"
    elif calories_burned * CAL_JOULE <  watt_hours_used * WATT_JOULE:
        return "Devices"
    else:
        return "Equal"

