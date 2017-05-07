import random
import math

MHEALTH = 200
ATK = 30

cc = 1
sc = 1
gc = 100

tcv = (cc * 1) + (sc * 100) + (gc * 500)

p = 0
lp = 0
hbp = 0
abp = 0
pp = 0
lpp = 0

shop = True

while shop:
    
    print '|------------------------------------------|'
    print '|               Dungeon Shop               |'
    print '|------------------------------------------|'
    print '| 1. Potion  2. Large Potion  3. HP Potion |'
    print '|  Cost: 50     Cost: 100       Cost: 300  |'
    print '|------------------------------------------|'
    print '|     4. ATK Potion   5. Poison Potion     |'
    print '|       Cost: 400          Cost: 50        |'
    print '|------------------------------------------|'
    print '|          6. Large Poison Potion          |'
    print '|                 Cost: 150                |'
    print '|------------------------------------------|'
    
    print 'Coins: {}'.format(tcv)
    
    ch = raw_input('Choose an item to buy: ')
    print''
    
    if ch == "1":
        ma = math.floor(tcv / 50)
        
        print 'Current Potions: {}'.format(p)
        print 'Max affordable: {}'.format(ma)
        
        con = input('How many: ')
        
        print ''
        
        qty = int(con)
        
        if qty > ma:
            print 'You cannot buy that many Potions!'
            print ''
        elif qty <= ma:
            print 'You bought {} Potion(s)!'.format(qty)
            
            tcv = tcv - (50 * qty)
            
            print 'Coins: {}'.format(tcv)
            print ''
            
            p = p + qty
    elif ch == "2":
        ma = math.floor(tcv / 100)
        
        print 'Current Large Potions: {}'.format(lp)
        print 'Max afforable: {}'.format(ma)
        
        con = raw_input('How many: ')
        
        print ''
        
        qty = int(con)
        
        if qty > ma:
            print 'You cannot buy that many Large Potions!'
            print ''
        elif qty <= ma:
            print 'You baught {} Large Potions!'.format(qty)
            
            tcv = tcv - (100 * qty)
            
            print 'Coins: {}'.format(tcv)
            print ''
            
            lp = lp + qty
    elif ch == "3":
        ma = math.floor(tcv / 300)
        
        print 'Current HP Potions: {}'.format(hbp)
        print 'Max afforable: {}'.format(ma)
        
        con = raw_input('How many: ')
        
        print ''
        
        qty = int(con)
        
        if qty > ma:
            print 'You cannot buy that many HP Potions!'
            print ''
        elif qty <= ma:
            print 'You baught {} HP Potions!'.format(qty)
            
            tcv = tcv - (300 * qty)
            
            print 'Coins: {}'.format(tcv)
            print ''
            
            hbp = hbp + qty
    elif ch == "4":
        ma = math.floor(tcv / 400)
        
        print 'Current ATK Potions: {}'.format(abp)
        print 'Max afforable: {}'.format(ma)
        
        con = raw_input('How many: ')
        
        print ''
        
        qty = int(con)
        
        if qty > ma:
            print 'You cannot buy that many ATK Potions!'
            print ''
        elif qty <= ma:
            print 'You baught {} ATK Potions!'.format(qty)
            
            tcv = tcv - (400 * qty)
            
            print 'Coins: {}'.format(tcv)
            print ''
            
            abp = abp + qty
    elif ch == "5":
        ma = math.floor(tcv / 50)
        
        print 'Current Poison Potions: {}'.format(lp)
        print 'Max afforable: {}'.format(ma)
        
        con = raw_input('How many: ')
        
        print ''
        
        qty = int(con)
        
        if qty > ma:
            print 'You cannot buy that many Poison Potions'
            print ''
        elif qty <= ma:
            print 'You baught {} Poison Potions!'.format(qty)
            
            tcv = tcv - (50 * qty)
            
            print 'Coins: {}'.format(tcv)
            print ''
            
            pp = pp + qty
    elif ch == "6":
        ma = math.floor(tcv / 150)
        
        print 'Current Large Poison Potions: {}'.format(lpp)
        print 'Max afforable: {}'.format(ma)
        
        con = raw_input('How many: ')
        
        print ''
        
        qty = int(con)
        
        if qty > ma:
            print 'You cannot buy that many Large Poison Potions'
            print ''
        elif qty <= ma:
            print 'You baught {} Large Poison Potions!'.format(qty)
            
            tcv = tcv - (150 * qty)
            
            print 'Coins: {}'.format(tcv)
            print ''
            
            lpp = lpp + qty
    
    p = p
    tcv = tcv
    lp = lp
    hbp = hbp
    abp = abp
    pp = pp
    lpp = lpp
    end = raw_input('Continue shopping (y or n): ')
    
    if end == "y":
        shop = True
    elif end == "n":
        shop = False

print ''
print 'Coins: {}'.format(tcv)
print 'Potions: {}'.format(p)
print 'Large Potions: {}'.format(lp)
print 'HP Potions: {}'.format(hbp)
print 'ATK Potions: {}'.format(abp)
print 'Poison Potions: {}'.format(pp)
print 'Large Poison Potions: {}'.format(lpp)
