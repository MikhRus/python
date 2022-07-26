#! python3
# Получает на вход строки "<текст>" и выводит в формате "* <текст>"
import pyperclip

text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i] # Добавляем звездочку и пробел в начало каждой строки
text = '\n'.join(lines)
pyperclip.copy(text)