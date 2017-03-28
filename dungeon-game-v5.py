import random

gc = 0
sc = 0
bc = 0
cc = 0
g = 0 
p = 0
r = 0
lp = 0
lr = 0

uH = 50

slaying = True

while slaying:
    dir = raw_input('Right or Left(r or l): ')
    lvl = random.randint(1,5)
    eH = 20 * lvl
    damage = random.randint( 10 * lvl, 20 * lvl)
    eDamage = random.randint( 5, 10)
    shop = random.randint(1,50)
    
    if dir == "r":
        print 'You chose right'
        
        a = random.randint(0, 20)
        
        if a <= 10:
            enemy = True
            print 'A level %s enemy appeared!' % (lvl)
            
            while enemy:
                atk = raw_input('Attack y or n? ')
                
                if atk == "y":
                    print 'You attack with %s points of damage, and took %d points of damage!' % (damage, eDamage)
                    print ''
                    uH = uH - eDamage
                    eH = eH - damage
                
                if atk == "n":
                    print 'You chose to wait and took %s points of damage!' % (eDamage)
                    print ''
                
                print 'Player health: %s' % (uH)
                print 'Enemy health: %s' % (eH)
                print ''
                
                if eH <= 0:
                    enemy = False
                    
                    print 'You hath slain the enemy!'
                    print ''
                    
                    isLoot = random.randint(1, 100)
                    
                    if 40 < isLoot < 65:
                        print 'You found some loot!'
                           
                        lType = random.randint(0, 3)
                        lQty = random.randint(1, 30)
                        lList = ['Gold Coins!', 'Silver Coins!', 'Bronze Coins!', 'Copper Coins!']
                        
                        if lType == 0:
                            gc = gc + lQty
                        elif lType == 1:
                            sc = sc + lQty
                        elif lType == 2:
                            bc = bc + lQty
                        elif lType == 3:
                            cc = cc + lQty
                        elif 4 <= lType <= 5:
                            g = g  + lQty
                        
                        print 'Gold coins: {}'.format(gc)
                        print 'silver coins: {}'.format(sc)
                        print 'Bronze coins: {}'.format(bc)
                        print 'Copper coins: {}'.format(cc)
                        print 'Gems: {}'.format(g)
                        print ''                        
                        
                    else:
                        print 'You found no loot.'
                        print ''
                    
                elif uH <= 0:
                    enemy = False
        
        elif a <= 20:
            enemy = False
            
            print 'There was no enemy to fight.'
            print ''
        
    
    if dir == "l":
        print 'You chose left'
        
        a = random.randint(0, 20)        
        
        if a <= 10:
            enemy = True
            print 'A level %s enemy appeared!' % (lvl)
            print ''
            
            while enemy:
                atk = raw_input('Attack y or n? ')
                
                if atk == "y":
                    print 'You attack with %s points of damage, and took %d points of damage!' % (damage, eDamage)
                    print ''
                    uH = uH - eDamage
                    eH = eH - damage
                
                if atk == "n":
                    print 'You chose to wait and took %s points of damage!' % (eDamage)
                    print ''
                
                print 'Player health: %s' % (uH)
                print 'Enemy health: %s' % (eH)
                print ''
                
                if eH <= 0:
                    enemy = False
                    
                    print 'You hath slain the enemy!'
                    print ''
                    
                    isLoot = random.randint(1, 100)
                    
                    if 40 < isLoot < 65:
                        print 'You found some loot!'
                           
                        lType = random.randint(0, 3)
                        lQty = random.randint(1, 30)
                        lList = ['Gold Coins!', 'Silver Coins!', 'Bronze Coins!', 'Copper Coins!']
                        
                        if lType == 0:
                            gc = gc + lQty
                        elif lType == 1:
                            sc = sc + lQty
                        elif lType == 2:
                            bc = bc + lQty
                        elif lType == 3:
                            cc = cc + lQty
                        elif 4 <= lType <= 5:
                            g = g  + lQty
                        
                        print 'Gold coins: {}'.format(gc)
                        print 'silver coins: {}'.format(sc)
                        print 'Bronze coins: {}'.format(bc)
                        print 'Copper coins: {}'.format(cc)
                        print 'Gems: {}'.format(g)
                        print ''
                    else:
                        print 'You found no loot.'
                        print ''
                    
                    print 'You hath slain the enemy!'
                    print ''
                elif uH <= 0:
                    enemy = False
    
    if 23 < shop < 27:
        print 'You hath found a shop!'
        sh = True
        
        while sh:
            print '|---------------------------------------|'
            print '|             Dungeon  Shop             |'
            print '|---------------------------------------|'
            print '| 1. Potion  2. Ration  3. Large Ration |'
            print '|  50 gems    50 gems       100 gems    |'
            print '|---------------------------------------|'
            print '| 4. Large Ration                       |'
            print '|    100 gems                           |'
            print '|---------------------------------------|'
            
            print ''
            
            item = raw_input('Pick an item to buy: ')
            print ''
            
            if item == '1':
                if g >= 50:
                    print 'You recieved 1 Potion.'
                    g = g - 50
                    p = p + 1
                else:
                    print 'You do not have enough gems.'
            elif item == '2':
                if g >= 50:
                    print 'You recieved 1 Ration.'
                    g = g - 50
                    r = r + 1
                else:
                    print 'You do not have enough gems.'
            elif item == '3':
                if g >= 100:
                    print 'You recieved 1 Large Potion.'
                    g = g - 100
                    lp = lp + 1
                else:
                    print 'You do not have enough gems.'
            elif item == '4':
                if g >= 100:
                    print 'YOu recieved 1 Large Ration.'
                    g = g - 100
                    lr = lr + 1
                else:
                    print 'You do not have enough gems.'
                
            g = g
            p = p
            r = r
            lp = lp
            lr = lr
            
            print 'Potions: {}'.format(p)
            print 'Rations: {}'.format(r)
            print 'Large Potions: {}'.format(lp)
            print 'Large Rations: {}'.format(lr)
            print 'Gems: {}'.format(g)
            print ''
            
            end = raw_input('End shop (y or n)? ')
            print ''
            
            if end == 'y':
               break
            elif end == 'n':
                shop = True
    else:
        print 'You hath not found a shop.'
        print ''
    print 'Potions: {}'.format(p)
    print 'Rations: {}'.format(r)
    print 'Large Potions: {}'.format(lp)
    print 'Large Rations: {}'.format(lr)
    
    print ''
    
    print 'Gold coins: {}'.format(gc)
    print 'silver coins: {}'.format(sc)
    print 'Bronze coins: {}'.format(bc)
    print 'Copper coins: {}'.format(cc)
    print 'Gems: {}'.format(g)
    print ''
    
    uH = uH
    gc = gc
    sc = sc
    bc = bc
    cc = cc
    g = g
    p = p
    r = r
    lp = lp
    lr = lr
        
    if uH <= 0:
        slaying = False
        
        print 'You have fallen in battle!'
        print ''

gcp = gc * 10
scp = sc * 7
bcp = bc * 5
ccp = cc * 3

tp = gcp + scp + bcp + ccp

print 'Gold Coin points: {}'.format(gcp)
print 'Silver Coin points: {}'.format(scp)
print 'Bronze Coin points: {}'.format(bcp)
print 'Copper Coin points: {}'.format(ccp)

print 'Total points: {}'.format(tp)
