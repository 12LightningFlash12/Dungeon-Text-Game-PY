import random

slaying = True

while slaying:
    dir = raw_input('Right or Left(r or l): ')
    lvl = random.randint(1,5)
    uH = 20
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
                    uH = uH - eDamage
                    eH = eH - damage
                
                if atk == "n":
                    print 'You chose to wait and took %s points of damage!' % (eDamage)
                
                print 'Player health: %s' % (uH)
                print 'Enemy health: %s' % (eH)
                
                if eH <= 0:
                    enemy = False
                    
                    print 'You hath slain the enemy!'
                    
                    else:
                        print 'You found no loot.'
                    
                elif uH <= 0:
                    enemy = False
        
        elif a <= 20:
            enemy = False
            
            print 'There was no enemy to fight.'
        
        
    if dir == "l":
        print 'You chose left'
        a = random.randint(0, 20)
        
        if a <= 10:
            enemy = True
            print 'A level %s enemy appeared!' % (lvl)
            
            while enemy:
                atk = raw_input('Attack y or n? ')
                
                if atk == "y":
                    print 'You attack with %s points of damage, and took %d points of damage!' % (damage, eDamage)
                    uH = uH - eDamage
                    eH = eH - damage
                
                if atk == "n":
                    print 'You chose to wait and took %s points of damage!' % (eDamage)
                
                print 'Player health: %s' % (uH)
                print 'Enemy health: %s' % (eH)
                
                if eH <= 0:
                    enemy = False
                    
                    print 'You hath slain the enemy!'
                    
                elif uH <= 0:
                    enemy = False
        
    if uH <= 0:
        slaying = False
        
        print 'You have fallen in battle!'
