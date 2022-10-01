import pyinputplus as pyip

order= []

prices = {'Цельнозерновой':10, 'Белый':15, 'Ржаной':12, 'Курица':50, 'Индейка':70, 'Ветчина':65, \
    'Тофу':90,'Чеддер':65,'Швейцарский':90,'Моцарелла':45,'да':30}
# Выбор хлеба
order.append(pyip.inputMenu(['Цельнозерновой', 'Белый', 'Ржаной'], \
    'Выберите хлеб:\n', numbered=True))
# Выбор мясной или типа начинки
order.append(pyip.inputMenu(['Курица', 'Индейка', 'Ветчина', 'Тофу'], \
                'Выберите белковую начинку:\n', numbered=True))
# Нужен сыр или нет?
needCheese = pyip.inputYesNo('Нужен сыр?\n', 'да', 'нет')
# Если нужен, то какой?
if needCheese == 'да':
    order.append(pyip.inputMenu(['Чеддер','Швейцарский','Моцарелла'], \
        'Выберите сыр:\n', numbered=True))
# Нужен ли соус?
order.append(pyip.inputYesNo('Нужен соус или помидор??\n', 'да', 'нет'))
# Сколько бутеров сделать? Мин 1
amount = pyip.inputInt('Сколько позиций сделать?\n', min=1)
# Подсчет стоимости блюда
cost = 0
for pos in order:
    cost += prices[pos]
# Вывод итоговой цены
print('Вы заказали %s бутерброд(-ов) на сумму %s' % (amount, cost*amount))
