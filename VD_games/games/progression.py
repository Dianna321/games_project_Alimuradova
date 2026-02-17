import random

DESCRIPTION = 'What number is missing in the progression?'

def get_question_and_answer():
    # Длина прогрессии от 5 до 10
    length = random.randint(5, 10)
    start = random.randint(1, 20)
    step = random.randint(2, 5)
    # Скрываем один элемент
    hidden_index = random.randint(0, length - 1)

    progression = []
    for i in range(length):
        value = start + i * step
        if i == hidden_index:
            progression.append('..')
            correct = str(value)
        else:
            progression.append(str(value))

    question = ' '.join(progression)
    return question, correct
