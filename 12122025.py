def update_inventory(inventory, shipment):
    products= [product[1] for product in inventory]
    for prod in shipment:
        if prod[1] in products:
            inventory[products.index(prod[1])][0] += prod[0]
        else:
            inventory.append(prod)
    return inventory
