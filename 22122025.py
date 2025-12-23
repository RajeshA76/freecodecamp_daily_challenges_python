def buy_items(funds, items):
    conv_rate = {
        'EUR': 1.10,
        'GBP': 1.25,
        'JPY': 0.007,
        'CAD': 0.75
    }
    currency = funds[1]
    if currency !=  'USD':
        amount = float(funds[0]) * conv_rate[currency]
    else:
        amount = float(funds[0])
    items_can_be_bought = 0
    
    for item in items:
        currency = item[1]
        if currency != 'USD':
            cost = float(item[0]) * conv_rate[currency]
        else:
            cost = float(item[0])
        if amount >= cost:
            items_can_be_bought += 1
            amount -= cost
        else:
            break
    
    if items_can_be_bought == len(items):
        return "Buy them all!"
    else:
        return f"Buy the first {items_can_be_bought} items."
        