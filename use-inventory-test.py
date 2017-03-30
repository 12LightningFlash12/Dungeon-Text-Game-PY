import random

enemy = True
MHEALTH = 100
uh = MHEALTH
eh = 100

p = 5
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
        
        uh = uh - ed
        eh = eh - ud
        
        print 'You took {0} points of damage, and gave {1} points of damage.'.format(ed, ud)
        print ''
    elif atk == 'n':
        inv = True
        
        while inv:
            uh = uh
            
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
                print 'You used a potion.'
                
                if uh == MHEALTH:
                    print 'The potion has no effect.'
                elif MHEALTH - uh >= 20:
                    print 'The potion heals you 20HP.'
                    
                    uh = uh + 20
                elif MHEALTH - uh <= 20:
                    e = MHEALTH - uh
                    
                    print 'The potion healed you {}HP'.format(e)
                    
                    uh = uh + e
                p = p - 1
                uh = uh
                print 'Health: {}'.format(uh)
            elif ch == 'ration':
                print 'You used a ration.'
                
                if uh == MHEALTH:
                    print 'The ration had no effect.'
                elif MHEALTH - uh >= 20:
                    print 'The ration heals you 20HP.'
                    
                    uh = uh + 20
                elif MHEALTH - uh <= 20:
                    e = MHEALTH - uh
                    
                    print 'The ration heals you {}HP.'.format(e)
                    
                    uh = uh + e
                
                r = r - 1
                uh = uh
                print 'Health: {}'.format(uh)
            elif ch == 'lpotion':
                print 'You used a large potion.'
                
                if uh == MHEALTH:
                    print 'The large potion had no effact.'
                elif MHEALTH - uh >= 50:
                    print 'The large potion heals you 50HP'
                    
                    uh = uh + 50
                elif MHEALTH - uh <= 50:
                    e = MHEALTH - uh
                    
                    print 'The large potion heals you {}HP.'.format(e)
                    
                    uh = uh + e
                lp = lr - 1
                uh = uh
                print 'Health: {}'.format(uh)
            
            end = raw_input('Stay y or n? ')
            
            if end == 'y':
                inv = True
            elif end == 'n':
                inv = False
    
    MHEALTH = MHEALTH
    uh = uh
    eh = eh
    
    p = p
    r = r
    
    print ''
    print 'Player health: {}'.format(uh)
    print 'Enemy health: {}'.format(eh)
    print ''
    print ''
    
    if uh <= 0:
        enemy = False
        print 'You hath fallen in battle.'
    elif eh <= 0:
        enemy = False
        print 'You hath slain the beast.'
