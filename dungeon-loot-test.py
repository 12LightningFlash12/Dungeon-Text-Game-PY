import random

isLoot = random.randint(1, 100)

print 'isLoot = %s' % (isLoot)

if 40 < isLoot < 65:
    print 'You found some loot!'
    
    lType = random.randint(0, 3)
    lQty = random.randint(1, 30)
    lList = ['Gold Coins!', 'Silver Coins!', 'Bronze Coins!', 'Copper Coins!']
    
    print 'You found %s' % (lQty), lList[lType]
else:
    print 'You found no loot.'
