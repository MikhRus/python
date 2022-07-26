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
    if len[word] == 0:
        pigLat.append[prefixNonLetters]
        continue
    # Определяем "небуквы" в конце слова
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]

