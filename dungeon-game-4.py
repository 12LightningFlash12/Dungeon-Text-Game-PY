import random

gc = 0
sc = 0
bc = 0
cc = 0
g = 0 
slaying = True

while slaying:
    dir = raw_input('Right or Left(r or l): ')
    lvl = random.randint(1,5)
    uH = 50
    eH = 20 * lvl
    damage = random.randint( 10 * lvl, 20 * lvl)
    eDamage = random.randint( 5, 10)
    
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
    
    print 'Gold coins: {}'.format(gc)
    print 'silver coins: {}'.format(sc)
    print 'Bronze coins: {}'.format(bc)
    print 'Copper coins: {}'.format(cc)
    print 'Gems: {}'.format(g)
    print ''
    
    gc = gc
    sc = sc
    bc = bc
    cc = cc
    g = g
        
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
