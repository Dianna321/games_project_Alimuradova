import prompt

ROUNDS = 3

def run_game(game):
    """
    Запускает игру, используя переданный модуль game,
    который должен содержать:
        DESCRIPTION: str - описание игры
        get_question_and_answer() -> (question, correct_answer)
    """
    print("Welcome to the VD Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(game.DESCRIPTION)

    for _ in range(ROUNDS):
        question, correct = game.get_question_and_answer()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ").strip().lower()

        if str(answer) != str(correct).lower():
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")
