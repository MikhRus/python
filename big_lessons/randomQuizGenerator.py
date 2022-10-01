#! python3
# randomQuizGenerator. ру - создает билеты с вопросами и ответами,
# расположенными в случайном порядке, вместе с ключами ответов
import random, os
from pathlib import Path

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',\
    'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',\
    'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',\
    'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',\
    'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',\
    'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta',\
    'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing',\
    'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City',\
    'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',\
    'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',\
    'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck',\
    'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem',\
    'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',\
    'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin',\
    'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond',\
    'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison',\
    'Wyoming': 'Cheyenne'}

#os.makedirs(str(Path.cwd()) + '/tickets')
# Генерирование 35 файлов билетов
for quizNum in range (35):
    # создание файлов билетов и ключей ответов

    quizFile = open(f'tickets/capitalquiz{quizNum + 1}.txt', 'w')
    answerKeyFile = open(f'tickets/capitalquiz_answers{quizNum + 1}', 'w')

    # запись заголовка билета
    quizFile.write('Имя:\n\nДата:\n\nГруппа:\n\n')
    quizFile.write((' '* 20) + f'Столицы штатов (билет {quizNum + 1})')
    quizFile.write('\n\n')

    # перемешиваем штаты
    states = list(capitals.keys())
    random.shuffle(states)

    # Организация цикла по всем 50 штатам
    # и создание вопроса для каждого из них
    for questionNum in range(50):
        # Получение правильных и неправильных ответов
        correctAnswer = capitals[states[questionNum]]
        wrongAnswer = list(capitals.values())
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        wrongAnswer = random.sample(wrongAnswer, 3)
        answerOptions = wrongAnswer + [correctAnswer]
        random.shuffle(answerOptions)

        # Запись вариантов ответов и вопросов в файлы
        quizFile.write(f'{questionNum + 1}. Выберите столицу штата {states[questionNum]}.\n')
        for i in range(4):
            quizFile.write(f"   {'ABCD'[i]}) {answerOptions[i]}\n")
            quizFile.write('\n')

        # записываем правильный ответ в файл
        answerKeyFile.write(f"{questionNum + 1}) {'ABCD'[answerOptions.index(correctAnswer)]}\n")

quizFile.close()
answerKeyFile.close()