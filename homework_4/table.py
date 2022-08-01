tableData = [['яблоки', 'апельсины', 'вишни', 'бананы'],
                ['Алиса', 'Боб', 'Кэрол', 'Дэвид'],
                ['собаки', 'кошки', 'лось', 'гусь']]

def printTable(data):
    colWidths = [0] * len(tableData)
    for list in data:
        for item in list:
            if len(item) > colWidths[data.index(list)]:
                colWidths[data.index(list)] = len(item)
        for item in list:
            print (item.rjust(colWidths[data.index(list)], '.'))
        # Как напечатать правильно?!?!?!?
    for i in range(len(tableData)):
        for j in range(len(i)):
            print()

printTable(tableData)

