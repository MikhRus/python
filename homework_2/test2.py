import random
list = [1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1]
totalStreaks = 0
streak = 0

for i in range(1,len(list)):
    if int(list[i]) == int(list[i-1]):
        streak += 1
        if streak >= 5:
            totalStreaks += 1          
    else:
        streak = 0
print('Total Streaks =', totalStreaks)

"""print(len(list))
for id, coin in enumerate(list):
    #print(coin, list[id-1], id)
    if int(coin) == int(list[id-1]):
        streak += 1
        if streak >= 5:
            totalStreaks += 1          
    else:
        streak = 0
print('Total Streaks =', totalStreaks)"""