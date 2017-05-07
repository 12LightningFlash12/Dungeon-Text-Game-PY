import random
import math

hp = 100000

ghp = 100
gatk = 10
gbhp = 500
gbatk = 30

shp = 100
satk = 15
sbhp = 400
sbatk = 30

uhp = 100
uatk = 10
ubhp = 600
ubatk = 30

sphp = 150
spatk = 15
spbhp = 1000
spbatk = 40

eIds = ['Goblin', 'Skeleton', 'Undead', 'Spirit']

eId = random.randint(0, 3)
eType = random.randint(1, 20)

if eType <= 15:
    print 'You found a base {}!'.format(eIds[eId])
    print ''
    
    if eId == 0:
        print 'Goblin health: {}'.format(ghp)
        print 'Goblin attack: {}'.format(gatk)
        print ''
    elif eId == 1:
        print 'Skeleton health: {}'.format(shp)
        print 'Skeleton Attack: {}'.format(satk)
        print ''
    elif eId == 2:
        print 'Undead health: {}'.format(uhp)
        print 'Undead attack: {}'.format(uatk)
        print ''
    else:
        print 'Spirit health: {}'.format(sphp)
        print 'Spirit attack: {}'.format(spatk)
        print ''
else:
    print 'You found a boss {}!'.format(eIds[eId])
    print ''
    
    if eId == 0:
        print 'Goblin Boss health: {}'.format(gbhp)
        print 'Goblin Boss attack: {}'.format(gbatk)
        print ''
    elif eId == 1:
        print 'Skeleton Boss health: {}'.format(sbhp)
        print 'Skeleton Boss Attack: {}'.format(sbatk)
        print ''
    elif eId == 2:
        print 'Undead Boss health: {}'.format(ubhp)
        print 'Undead Boss attack: {}'.format(ubatk)
        print ''
    else:
        print 'Spirit Boss health: {}'.format(spbhp)
        print 'Spirit Boss attack: {}'.format(spbatk)
        print ''
