# счетчики и переменные
correct_answer_counter = 0
all_score = 0
attempt = 3

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

#цикл с попытками
    while attempt > 0:
      user_answers = input(f'{questions[i]} ')

      if user_answers == answers[i]:
        correct_answer_counter += 1
        all_score += attempt

        print('Ответ верный!')
        break

      attempt -= 1

      if attempt > 0:
        print(f'Осталось попыток: \x1B[3m{attempt}\x1B[0m, попробуйте еще раз!')

      elif attempt == 0:
        print(f'Неправильно. Правильный ответ: \x1B[3m{answers[i]}\x1B[0m')

# округленный процент ответов
  correct_answer_percent = round(100 / len(questions) *
  correct_answer_counter)

#итог
  print(f'''Вот и всё!
Вы ответили на {correct_answer_counter} вопросов из {len(questions)} верно, вы набрали {all_score} баллов.''')

#если все пошло не по плану =)
else:
  print('Кажется, вы не хотите играть. Очень жаль. =(')
