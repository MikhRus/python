import random
list = []
totalStreaks = 0
streak = 0
#Filling list
for i in range(20):
    list.append(random.randint(0,1))
for i in range(1,len(list)):
    if int(list[i]) == int(list[i-1]):
        streak += 1
        if streak >= 5:
            totalStreaks += 1          
    else:
        streak = 0

print(list)
print('Total Streaks =', totalStreaks)