inventory = {'Hammer' : 1, 'Axe' : 10 , 'Knife' : 20, 'Gold Coin': 100}

dragonLoot = ['Gold Coin', 'Gun', 'Monster\'s head', 'Gold Coin', 'Axe', 'Gold Coin']

def displayInventory(inv):
    totalStuff = 0
    print('Inventory:')
    for k, v in inv.items():
        print(' ', k, '-', v)
        totalStuff += v
    print('Total stuffs:', totalStuff)

def addToInventory(inv, newItems):
    newStuff = {}
    for item in newItems:
        newStuff.setdefault(item,0)
        newStuff[item]+=1
        #print(newStuff)
    #for kInv, vInv in inv.Items():
    for kItem, vItem in newStuff.items():
        if kItem in inv:
            inv[kItem] += vItem
        else:
            inv[kItem] = vItem
    #print(newStuff)

    return inv

inventory = addToInventory(inventory, dragonLoot)
displayInventory(inventory)