#! python3
# mcb.pyw - сохраняет и загружает фрагменты текста в буфер обмена
#
# Использование: ру.ехе mcb.pyw save <ключевое_слово> - сохраняет
#                   содержимое буфера обмена с ключевым словом
#               ру.ехе mcb.pyw <ключевое_слово> - загружает текст,
#                   соответствующий ключевому слову, в буфер обмена
#               ру.ехе mcb.pyw list - загружает все ключевые слова
#                   в буфер обмена

import sys, shelve, pyperclip

mcbShelf = shelve.open('big_lessons/mcb')

# Сохранение текста из буфера обмена
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        #print(sys.argv[1], sys.argv[2])
        #print(pyperclip.paste())
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]
        #print(str(list(mcbShelf.keys())))

elif len(sys.argv) == 2:
    # Формирование списка ключевых слов и загрука сохраненного содержимого 
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        #print(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        for i in mcbShelf:
            del mcbShelf[i]
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    
mcbShelf.close()
