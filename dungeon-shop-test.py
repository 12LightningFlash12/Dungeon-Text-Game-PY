gems = 1000
shop = True

while shop:
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
        if gems >= 50:
            print 'You recieved 1 Potion.'
            gems = gems - 50
        else:
            print 'You do not have enough gems.'
    elif item == '2':
        if gems >= 50:
            print 'You recieved 1 Ration.'
            gems = gems - 50
        else:
            print 'You do not have enough gems.'
    elif item == '3':
        if gems >= 100:
            print 'You recieved 1 Large Potion.'
            gems = gems - 100
        else:
            print 'You do not have enough gems.'
    elif item == '4':
        if gems >= 100:
            print 'YOu recieved 1 Large Ration.'
            gems = gems - 100
        else:
            print 'You do not have enough gems.'
    
    gems = gems
    
    print 'Gems: {}'.format(gems)
    print ''
    
    end = raw_input('End shop (y or n)? ')
    print ''
    
    if end == 'y':
        shop = False
    elif end == 'n':
        shop = True

