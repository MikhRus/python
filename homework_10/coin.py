import random

guess = ''
while guess not in ('орел', 'решка'):
    print ('Угадайте результат! Введите "орел" или "решка":')
    guess = input()

toss = random.choice(('орел', 'решка')) # 0 - решка, 1 - орел
if toss == guess:
    print('Угадали!')
else:
    print('Увы! Попробуйте снова!')
    guess = input()
    if toss == guess:
        print('Угадали!')
    else:
        print('Нет. Вам не везет в этой игре.')