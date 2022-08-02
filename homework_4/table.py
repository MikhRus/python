tableData = [['яблоки', 'апельсины', 'вишни', 'бананы'],
                ['Алиса', 'Боб', 'Кэрол', 'Дэвид'],
                ['собаки', 'кошки', 'лось', 'гусь']]

def printTable(data):
    colWidths = [0] * len(tableData)
    for list in data:
        for item in list:
            if len(item) > colWidths[data.index(list)]:
                colWidths[data.index(list)] = len(item)
        #for item in list:
            #print (item.rjust(colWidths[data.index(list)], '.'))
        # Как напечатать правильно?!?!?!?
    for i in range(len(tableData[0])):
        print(str(data[0][i]).rjust(colWidths[0]) + ' ' + str(data[1][i]).rjust(colWidths[1]) + \
        ' ' + str(data[2][i]).rjust(colWidths[2]))

printTable(tableData)

