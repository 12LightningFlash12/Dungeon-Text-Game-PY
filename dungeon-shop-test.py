gems = 1000
shop = True

p = 0
r = 0
lp = 0
lr = 0
hpp = 0

while shop:
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
        if gems >= 50:
            print 'You recieved 1 Potion.'
            gems = gems - 50
            p = p + 1
        else:
            print 'You do not have enough gems.'
    elif item == '2':
        if gems >= 50:
            print 'You recieved 1 Ration.'
            gems = gems - 50
            r = r + 1
        else:
            print 'You do not have enough gems.'
    elif item == '3':
        if gems >= 100:
            print 'You recieved 1 Large Potion.'
            gems = gems - 100
            lp = lp + 1
        else:
            print 'You do not have enough gems.'
    elif item == '4':
        if gems >= 100:
            print 'YOu recieved 1 Large Ration.'
            gems = gems - 100
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
    
    gems = gems
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
    print 'Gems: {}'.format(gems)
    print ''
    
    end = raw_input('End shop (y or n)? ')
    print ''
    
    if end == 'y':
        shop = False
    elif end == 'n':
        shop = True

print 'Potions: {}'.format(p)
print 'Rations: {}'.format(r)
print 'Large Potions: {}'.format(lp)
print 'Large Rations: {}'.format(lr)
print 'HP Potions: {}'.format(hpp)
print 'Gems: {}'.format(gems)
print ''
