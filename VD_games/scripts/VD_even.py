import prompt
import random

def main():
    print("Welcome to the VD-games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    rounds = 0
    while rounds < 3:
        number = random.randint(1, 100)
        correct = "yes" if number % 2 == 0 else "no"
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ").strip().lower()
        if answer == correct:
            print("Correct!")
            rounds += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")

if __name__ == "__main__":
    main()
