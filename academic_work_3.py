# счетчики для ответов и вопросов
correct_answer_counter = 0
question_counter = 0

# вопросы и ответы
questions = ["My name ___  Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]

# приветствие и проверка готовности
user_check = input('''Привет!
Предлагаю проверить свои знания английского!
Наберите "ready", чтобы начать! ''')

# по чек-листу если при старте программы нажать клавишу Enter,
#программа начинает задавать вопросы,
#поэтому добавил пустую строку в проверку,
#возможно не так полнял задание
if user_check.lower() == "ready" or user_check == "":

# блок вопросов
  for i in range(len(questions)):

    user_answers = input(f'{questions[i]} ')
    question_counter = i + 1

    if user_answers == answers[i]:
      correct_answer_counter += 1

      print('Ответ верный!')

    else:
      print(f'Неправильно. Правильный ответ: \x1B[3m{answers[i]}\x1B[0m')

# округленный процент ответов
  correct_answer_percent = round(100 / question_counter *
  correct_answer_counter)

#итог
  print(f'''Вот и всё!
Вы ответили на {correct_answer_counter} вопросов из {question_counter} верно, это {correct_answer_percent} процентов.''')

#если все пошло не по плану =)
else:
  print('Кажется, вы не хотите играть. Очень жаль. =(')
