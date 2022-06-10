inventory = {
    'Rope' : 1,
    'Torch' : 6,
    'Gold Coins' : 42,
    'Dagger' : 1,
    'Arrow' : 12,
}

empty_inv = {}

def print_inventory(x):
    print ('Inventory:')
    total_items = 0
    for key, val in x.items():
        total_items += val
        print(str(val) + ' ' + key)
    print('You have ' + str(total_items) + ' items in total')

print_inventory(inventory)

dragonLoot = ['Gold Coins', 'Dagger', 'Gold Coins', 'Gold Coins', 'Ruby']

def add_to_inventory(inv, loot):
    for i in loot:
        if i in inv.keys():
            inv[i] += 1
        else:
            inv.update({i : 1})
    print_inventory(inv)


add_to_inventory(empty_inv, dragonLoot)