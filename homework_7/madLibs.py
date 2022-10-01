#! python3
# Заменяет в тектовых файлах слова 'ПРИЛАГАТЕЛЬНОЕ', 'СУЩЕСТВИТЕЛЬНОЕ', 'НАРЕЧИЕ' или 'ГЛАГОЛ'
# на нужные пользователю и сохраняет их в новый файл
import os, re
# Открытие файлов
inFile = open('./homework_7/hw7_1.txt', 'r')
outFile = open('./homework_7/hw7_1_new.txt', 'w')
# Чтение исходного файла в строку
stringForChange = inFile.read()
# Поиск необходимых слов для замены
wordRegex = re.compile(r'ПРИЛАГАТЕЛЬНОЕ|СУЩЕСТВИТЕЛЬНОЕ|ГЛАГОЛ|НАРЕЧЬЕ')
words = wordRegex.findall(stringForChange)

# Замена слов на введеные пользователем
for word in words:
    print(f'Введите {word}:\n')
    stringForChange = wordRegex.sub(input(), stringForChange, 1)

print(stringForChange) 
outFile.write(stringForChange)

inFile.close()
outFile.close()
