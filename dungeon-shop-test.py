gems = 1000
shop = True

while shop:
    print '|---------------------------------------|'
    print '|             Dungeon  Shop             |'
    print '|---------------------------------------|'
    print '| 1. Potion  2. Ration  3. Large Ration |'
    print '|  50 gems   100 gems       200 gems    |'
    print '|---------------------------------------|'
    
    print ''
    
    item = raw_input('Pick an item to buy: ')
    print ''
    
    if item == '1':
        if gems >= 50:
            print 'You recieved 1 potion.'
            
            gems = gems - 50
        else:
            print 'You do not have enough gems.'
    elif item == '2':
        if gems >= 100:
            print 'You recieved 1 Ration.'
            
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

