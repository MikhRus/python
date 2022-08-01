# Ковертирует текст в поросячую латынь (лул шо?)
print('Введите предложение на английском языке для перевода его в поросячую латынь.')
message = input()

VOWELS = {'a', 'o', 'e', 'i', 'y', 'u'} # Vowels - гласные

pigLat = []

for word in message.split():
    # Определяем "небуквы" в начале слова
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha:
        prefixNonLetters += word[0]
        word = word[1:]
    if len(word) == 0:
        pigLat.append[prefixNonLetters]
        continue
    # Определяем "небуквы" в конце слова
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]
    # Запоминаем регистр слов
    wasUpper = word.isupper()
    wasTitel = word.istitle()
    word = word.lower() # перевод в нижний регистр
    # Отделяем согласные в начале слова
    prefixConstants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConstants += word[0]
        word = word[1:]
    # Присоединяем в правильной последовательности
    if prefixConstants != '':
        word += prefixConstants + 'ay'
    else:
        word += 'yay'
    # Возвращаем исходный регистр
    if wasUpper:
        word = word.upper()
    if wasTitel:
        word = word.title()
    # Возвращаем небуквенные символы в начало или конец слова
    pigLat.append(prefixNonLetters + word + suffixNonLetters)
# Соединяем слова обратно в строку
print(' '.join(pigLat))

    

