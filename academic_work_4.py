# словари
words_easy = {
    "family":"семья",
    "hand": "рука",
    "people":"люди",
    "evening": "вечер",
    "minute":"минута",
}

words_medium = {
    "believe":"верить",
    "feel": "чувствовать",
    "make":"делать",
    "open": "открывать",
    "think":"думать",
}

words_hard  = {
    "rural":"деревенский",
    "fortune": "удача",
    "exercise":"упражнение",
    "suggest": "предлагать",
    "except":"кроме",
}

levels = {
   0: "Нулевой",
   1: "Так себе",
   2: "Можно лучше",
   3: "Норм",
   4: "Хорошо",
   5: "Отлично",
}

answers = {}

# словарь для решения пользователя
level_dict = {'легкий':words_easy, 'средний':words_medium, 'сложный':words_hard}

# цикл на выбор сложности
while True:

    user_level = input('''Выберите уровень сложности.
Легкий, средний, сложный.
''')
# выбор словаря из решения пользователя

    if user_level.lower() in level_dict.keys():
        words = level_dict[user_level.lower()]
        break

    else:
        print('Сложность не распознана')

print(f'Уровень сложности выбран, мы предложим {len(words)} слов, подберите перевод.')

# цикл на проверкуввод Enter с условиями выхода
while True:

    user_start = input('Нажмите Enter чтобы начать.')

    if user_start == '':

        # цикл на вопрос/ответ и запись результата
        for en_word, ru_word in words.items():

            check_answers = input(f''' - {en_word.title()}, {len(ru_word)} букв, начинается на {ru_word[0]}...
            ''')

            if check_answers.lower() == ru_word.lower():
                answers[en_word] = True
                print(f'Верно, {en_word} — это {ru_word}.')

            else:
                answers[en_word] = False
                print(f'Неверно, {en_word} — это {ru_word}.')
        break
    else:
        print('Удалите символы чтобы начать')

# цикл угаданных слов
print('Правильно отвеченные слова: ')
for en_word, bool_answer in answers.items():
    if bool_answer == True:
        print(en_word)

# цикл неугаданных слов
print(f'Неправильно отвечены слова: ')
for en_word, bool_answer in answers.items():
    if bool_answer == False:
        print(en_word)

# вывод ранга
print(f'''Ваш ранг:
{levels[sum(answers.values())]}''')
