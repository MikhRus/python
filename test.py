import random

#print(random.randrange(0,2))

if int(random.randrange(0,2)) == 1:
    print('true')
else:
    print('false')

print(bool(random.randint(0,1)))