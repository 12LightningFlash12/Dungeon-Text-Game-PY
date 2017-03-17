import random

dir = random.randint(0, 100)

print dir

if dir <= 10:
    print "left"
elif dir <= 20:
    print "right"
