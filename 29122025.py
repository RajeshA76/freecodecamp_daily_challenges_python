def fuel_to_add(current_gallons, required_liters):
    to_gallons = required_liters / 3.78541
    gallons_needed = int(to_gallons - current_gallons) + 1
    return max(gallons_needed, 0)