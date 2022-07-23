import imp
from ipaddress import collapse_addresses


import random, time, copy
WIDTH = 60
HEIGHT = 20

# Create new line
nextCells = []
for x in range(WIDTH):
    column = [] #Create new column
    for y in range(HEIGHT):
        # Random filling table
        if random.randint(0,1) == 0:
            column.append('#') # Add alive cell
        else:
            column.append(' ') # Add dead cell
    nextCells.append(column) # Add filled column into line

while True: # Main cycle
    print('\n\n\n\n\n') # Split steps
    currentCells = copy.deepcopy(nextCells) # Copy table into new memory cell
    # Print table
    for x in range(WIDTH):
        for y in range(HEIGHT):
            print(currentCells[x][y], end = '')
        print()
    # Calc new cells for next step
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neigh coords
            leftCoord  = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # Вычисление количества живых соседних клеток
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 # жива соседняя клетка # слева сверху                                   
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 # жива соседняя клетка сверху
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # жива соседняя клетка # справа сверху
            if currentCells[leftCoord] [y] == '#':
                numNeighbors += 1 # жива соседняя клетка слева
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 # жива соседняя клетка справа
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # жива соседняя клетка # слева снизу
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 # жива соседняя клетка снизу
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 # жива соседняя клетка # справа снизу

            # Изменение клетки на основе правил игры "Жизнь"
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                # Живые клетки с двумя или тремя живыми # соседями остаются живыми
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # Мертвые клетки с тремя живыми соседями оживают
                nextCells[x][y] = '#'
            else:
                # Все остальные клетки умирают или остаются мертвыми
                nextCells[x][y] = ' ' 
    time.sleep(1) # добавим секундную паузу,
# чтобы уменьшить мерцание
