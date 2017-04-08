import random

uH = 100
eH = 100
bH = 200

eD = random.randint(10, 40)
uD = random.randint(20, 50)
bD = random.randint(40, 60)

game = True

a = 0

while game:
    eType = random.randint(0, 100)
    
    a = a + 1
    
    a = a
    
    if 0 <= eType <= 97:
        game = True
    elif 97 <= eType <= 100:
        game = False

a = a

print 'A: {}'.format(a)
