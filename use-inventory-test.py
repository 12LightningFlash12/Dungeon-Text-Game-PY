import random

enemy = True
MHEALTH = 100
uH = MHEALTH
eh = 100

p = 1
r = 5
lp = 5
lr = 5
hpp = 5

print 'An enemy appeared!'

while enemy:
    ud = random.randint(10, 40)
    ed = random.randint(10, 30)
    
    atk = raw_input('Attack y or n? ')
    print ''
    
    if atk == 'y':
        print 'You chose to attack!'
        
        uH = uH - ed
        eh = eh - ud
        
        print 'You took {0} points of damage, and gave {1} points of damage.'.format(ed, ud)
        print ''
    elif atk == 'n':
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
                if lr >0:
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
    
    MHEALTH = MHEALTH
    uH = uH
    eh = eh
    
    p = p
    r = r
    
    print ''
    print 'Player health: {}'.format(uH)
    print 'Enemy health: {}'.format(eh)
    print ''
    print ''
    
    if uH <= 0:
        enemy = False
        print 'You hath fallen in battle.'
    elif eh <= 0:
        enemy = False
        print 'You hath slain the beast.'
