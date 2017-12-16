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
hpp = 0

MHEALTH = 100

uH = MHEALTH

bH = 200

slaying = True

while slaying:
    dir = raw_input('Right, Left, or Foward: ')
    lvl = random.randint(1,5)
    eH = 50 * lvl
    shop = random.randint(1,35)
    
    print 'You chose: {0}'.format(dir)
    
    a = random.randint(0, 40)
    
    if a <= 10:
        enemy = True
        print 'A level {0} enemy appeared!'.format(lvl)
        
        while enemy:
            atk = raw_input('Attack y or n? ')
            
            if atk == "Y" or atk == "y" or atk == "yes" or atk == "Yes" or atk == "YES":
                damage = random.randint(10 * lvl, 20 * lvl)
                eDamage = random.randint(5, 10)
                
                print 'You attack with {0} points of damage, and took {1} points of damage!'.format(damage, eDamage)
                print ''
                uH = uH - eDamage
                eH = eH - damage
            if atk == "n" or atk == "N" or atk == "no" or atk == "No" or atk == "NO":
                inv = True
                
                while inv:
                    uH = uH
                    
                    print '|---------------------------------|'
                    print '|            INVENTORY            |'
                    print '|---------------------------------|'
                    print '|     Potion: {0}     Ration: {1}     |'.format(p, r)
                    print '|---------------------------------|'
                    print '| Large Potion: {0} Large Ration: {1} |'.format(lp, lr)
                    print '|---------------------------------|'
                    print '| HP Potion: {0}                    |'.format(hpp)
                    print '|---------------------------------|'
                    ch = raw_input('Choose an item to use: ')
                    print ''
                    
                    if ch == 'potion':
                        if p > 0:
                            print 'You used a potion.'
                            
                            if uH == MHEALTH:
                                print 'The potion has no effect.'
                            elif MHEALTH - uH >= 20:
                                print 'The potion heals you 20HP.'
                                
                                uH = uH + 20
                            elif MHEALTH - uH <= 20:
                                e = MHEALTH - uH
                                
                                print 'The potion healed you {}HP'.format(e)
                                
                                uH = uH + e
                            p = p - 1
                            uH = uH
                            print 'Health: {}'.format(uH)
                        else:
                            print 'You do not have enough potions.'
                    elif ch == 'ration':
                        if r > 0:
                            print 'You used a ration.'
                            
                            if uH == MHEALTH:
                                print 'The ration had no effect.'
                            elif MHEALTH - uH >= 20:
                                print 'The ration heals you 20HP.'
                                
                                uH = uH + 20
                            elif MHEALTH - uH <= 20:
                                e = MHEALTH - uH
                                
                                print 'The ration heals you {}HP.'.format(e)
                                
                                uH = uH + e
                            
                            r = r - 1
                            uH = uH
                            print 'Health: {}'.format(uH)
                        else:
                            print 'You do not have enought rations.'
                    elif ch == 'lpotion':
                        if lp > 0:
                            print 'You used a large potion.'
                            
                            if uH == MHEALTH:
                                print 'The large potion had no effact.'
                            elif MHEALTH - uH >= 50:
                                print 'The large potion heals you 50HP'
                                
                                uH = uH + 50
                            elif MHEALTH - uH <= 50:
                                e = MHEALTH - uH
                                
                                print 'The large potion heals you {}HP.'.format(e)
                                
                                uH = uH + e
                            lp = lp - 1
                            uH = uH
                            print 'Health: {}'.format(uH)
                        else:
                            print 'You do not have enought large potions.'
                    elif ch == 'lration':
                        if lr > 0:
                            print 'You used a large ration.'
                            
                            if uH == MHEALTH:
                                print 'The large ration had no effact.'
                            elif MHEALTH - uH >= 50:
                                print 'The large ration heals you 50HP'
                                
                                uH = uH + 50
                            elif MHEALTH - uH <= 50:
                                e = MHEALTH - uH
                                
                                print 'The large ration heals you {}HP.'.format(e)
                                
                                uH = uH + e
                            lr = lr - 1
                            uH = uH
                            print 'Health: {}'.format(uH)
                        else:
                            print 'You do not have enough large rations.'
                    elif ch == 'hppotion':
                        if hpp > 0:
                            print 'You used a HP Potion.'
                            print 'Your Max Health was raised 20HP.'
                            print ''
                            
                            MHEALTH = MHEALTH + 20
                            print 'Max health: {}'.format(MHEALTH)
                            
                            hpp = hpp - 1
                        else:
                            print 'You do not have enough HP potions.'
                    end = raw_input('Stay y or n? ')
                    
                    if end == 'y':
                        inv = True
                    elif end == 'n':
                        inv = False
                    
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
                slaying = False
    elif a <= 20:
        enemy = False
        
        print 'There was no enemy to fight.'
        print ''
    elif a >= 37:
        boss = True
        
        print 'You found a boss!'
        
        while boss:
            atk = raw_input('Attack (y or n): ')
            damage = random.randint(10 * lvl, 20 * lvl)
            bDamage = random.randint(20, 30)
            
            if atk == "Y" or atk == "y" or atk == "yes" or atk == "Yes" or atk == "YES":
                print 'You attack with {0} points of damage! You took {1} pooints of damage!'.format(damage, bDamage)
                print ''
                
                uH = uH - bDamage
                bH = bH - damage
            if atk == "n" or atk == "N" or atk == "no" or atk == "No" or atk == "NO":
                inv = True
                
                while inv:
                    uH = uH
                    
                    print '|---------------------------------|'
                    print '|            INVENTORY            |'
                    print '|---------------------------------|'
                    print '|     Potion: {0}     Ration: {1}     |'.format(p, r)
                    print '|---------------------------------|'
                    print '| Large Potion: {0} Large Ration: {1} |'.format(lp, lr)
                    print '|---------------------------------|'
                    print '| HP Potion: {0}                    |'.format(hpp)
                    print '|---------------------------------|'
                    ch = raw_input('Choose an item to use: ')
                    print ''
                    
                    if ch == 'potion':
                        if p > 0:
                            print 'You used a potion.'
                            
                            if uH == MHEALTH:
                                print 'The potion has no effect.'
                            elif MHEALTH - uH >= 20:
                                print 'The potion heals you 20HP.'
                                
                                uH = uH + 20
                            elif MHEALTH - uH <= 20:
                                e = MHEALTH - uH
                                
                                print 'The potion healed you {}HP'.format(e)
                                
                                uH = uH + e
                            p = p - 1
                            uH = uH
                            print 'Health: {}'.format(uH)
                        else:
                            print 'You do not have enough potions.'
                    elif ch == 'ration':
                        if r > 0:
                            print 'You used a ration.'
                            
                            if uH == MHEALTH:
                                print 'The ration had no effect.'
                            elif MHEALTH - uH >= 20:
                                print 'The ration heals you 20HP.'
                                
                                uH = uH + 20
                            elif MHEALTH - uH <= 20:
                                e = MHEALTH - uH
                                
                                print 'The ration heals you {}HP.'.format(e)
                                
                                uH = uH + e
                            
                            r = r - 1
                            uH = uH
                            print 'Health: {}'.format(uH)
                        else:
                            print 'You do not have enought rations.'
                    elif ch == 'lpotion':
                        if lp > 0:
                            print 'You used a large potion.'
                            
                            if uH == MHEALTH:
                                print 'The large potion had no effact.'
                            elif MHEALTH - uH >= 50:
                                print 'The large potion heals you 50HP'
                                
                                uH = uH + 50
                            elif MHEALTH - uH <= 50:
                                e = MHEALTH - uH
                                
                                print 'The large potion heals you {}HP.'.format(e)
                                
                                uH = uH + e
                            lp = lp - 1
                            uH = uH
                            print 'Health: {}'.format(uH)
                        else:
                            print 'You do not have enought large potions.'
                    elif ch == 'lration':
                        if lr > 0:
                            print 'You used a large ration.'
                            
                            if uH == MHEALTH:
                                print 'The large ration had no effact.'
                            elif MHEALTH - uH >= 50:
                                print 'The large ration heals you 50HP'
                                
                                uH = uH + 50
                            elif MHEALTH - uH <= 50:
                                e = MHEALTH - uH
                                
                                print 'The large ration heals you {}HP.'.format(e)
                                
                                uH = uH + e
                            lr = lr - 1
                            uH = uH
                            print 'Health: {}'.format(uH)
                        else:
                            print 'You do not have enough large rations.'
                    elif ch == 'hppotion':
                        if hpp > 0:
                            print 'You used a HP Potion.'
                            print 'Your Max Health was raised 20HP.'
                            print ''
                            
                            MHEALTH = MHEALTH + 20
                            print 'Max health: {}'.format(MHEALTH)
                            
                            hpp = hpp - 1
                        else:
                            print 'You do not have enough HP potions.'
                    
                    end = raw_input('Stay y or n? ')
                    
                    if end == 'y':
                        inv = True
                    elif end == 'n':
                        inv = False
            print 'Player health: {0}'.format(uH)
            print 'Boss health  : {0}'.format(bH)
            print ''
            
            if bH <= 0:
                boss = False
                
                print 'You hath slain the BOSS!'
                print ''
                
                isLoot = random.randint(1, 100)
                
                if 30 < isLoot < 70:
                    lType = random.randint(0,5)
                    lList = ['Gold Coins', 'Silver Coins', 'Bronze Coins', 'Copper Coins', 'Gems']
                    lQty = random.randint(60, 80)
                    
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
                boss = False
                slaying = False
    else:
        print 'There was no enemy to fight.'
        print ''
    
    if 20 < shop < 27:
        print 'You hath found a shop!'
        sh = True
        
        while sh:
            print '|---------------------------------------|'
            print '|             Dungeon  Shop             |'
            print '|---------------------------------------|'
            print '| 1. Potion  2. Ration  3. Large Ration |'
            print '|  50 gems    50 gems       100 gems    |'
            print '|---------------------------------------|'
            print '| 4. Large Ration  5. HP Potion         |'
            print '|    100 gems        300 gems           |'
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
            elif item == '5':
                if gems >= 300:
                    print 'You recieved 1 HP Potion.'
                    gems = gems - 300
                    hpp = hpp + 1
                else:
                    print 'You do not have enough gems.'
                
            g = g
            p = p
            r = r
            lp = lp
            lr = lr
            hpp = hpp
            
            print 'Potions: {}'.format(p)
            print 'Rations: {}'.format(r)
            print 'Large Potions: {}'.format(lp)
            print 'Large Rations: {}'.format(lr)
            print 'HP Potions: {}'.format(hpp)
            print 'Gems: {}'.format(g)
            print ''
            
            end = raw_input('End shop (y or n)? ')
            print ''
            
            if end == 'y':
               shop == False
            elif end == 'n':
                shop = True
    else:
        print 'You hath not found a shop.'
        print '
    print 'Potions: {}'.format(p)
    print 'Rations: {}'.format(r)
    print 'Large Potions: {}'.format(lp)
    print 'Large Rations: {}'.format(lr)
    print 'HP Potions: {}'.format(hpp)
    
    print ''
    
    print 'Gold coins: {}'.format(gc)
    print 'silver coins: {}'.format(sc)
    print 'Bronze coins: {}'.format(bc)
    print 'Copper coins: {}'.format(cc)
    print 'Gems: {}'.format(g)
    print ''
    
    uH = uH
    bH = bH
    gc = gc
    sc = sc
    bc = bc
    cc = cc
    g = g
    p = p
    r = r
    lp = lp
    lr = lr
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
