import random

gc = 0
sc = 0
bc = 0
cc = 0
g = 0

loop = True

while loop:
    lType = random.randint(0,5)
    lList = ['Gold Coins', 'Silver Coins', 'Bronze Coins', 'Copper Coins', 'Gems']
    lQty = random.randint(1, 19)
    
    if lType == 0:
        gc = gc + lQty
    elif lType == 1:
        sc = sc + lQty
    elif lType == 2:
        bc = bc + lQty
    elif lType == 3:
        cc = cc + lQty
    elif 4 < lType < 5:
        g = g  + lQty
    
    print 'Gold coins: {}'.format(gc)
    print 'silver coins: {}'.format(sc)
    print 'Bronze coins: {}'.format(bc)
    print 'Copper coins: {}'.format(cc)
    print 'Gems: {}'.format(g)
    print ''
    
    lEnd = raw_input('End the Loop(y or n): ')
    
    print ''
    
    if lEnd == 'y':
        loop = True
    elif lEnd == 'n':
        loop = False
    
