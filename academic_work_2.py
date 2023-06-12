# счетчик для ответов
correct_answer_counter = 0

# знакомство
user_name = input('''Привет! Предлагаю проверить свои знания английского!
Напиши, как тебя зовут.
''')
print(f"Привет, {user_name}, начинаем тренировку!")

# первый вопрос
question_1 = input("My name ___ Vova.")
if question_1 == "is":
    correct_answer_counter += 1
    print('''Ответ верный!
Вы получаете 10 баллов!''')
else:
    print('''Неправильно.
Правильный ответ: is''')

# второй вопрос
question_2 = input("I ___ a coder.")
if question_2 == "am":
    correct_answer_counter += 1
    print('''Ответ верный!
Вы получаете 10 баллов!''')
else:
    print('''Неправильно.
Правильный ответ: am''')

# третий вопрос
question_3 = input("I live ___ Moscow.")
if question_3 == "in":
    correct_answer_counter += 1
    print('''Ответ верный!
Вы получаете 10 баллов!''')
else:
    print('''Неправильно.
Правильный ответ: in''')

# округленный процент ответов через переменную
all_question = round(100 / 3 * correct_answer_counter)

# кол-во баллов
total_score = correct_answer_counter * 10

# итог
print(f'Вот и всё, {user_name}!')


if correct_answer_counter == 1:
    print ('Вы ответили на 1 вопрос из 3 верно.')
elif correct_answer_counter == 2 or correct_answer_counter == 3:
    print (f'Вы ответили на {correct_answer_counter} вопроса из 3 верно.')
elif correct_answer_counter == 0:
    print (f'У Вас нет верных ответов.')

print(f'''Вы заработали {total_score} баллов.
Это {all_question} процентов.''')
