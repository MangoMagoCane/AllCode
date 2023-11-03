import random
import sys

def main():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")

    number = random.randint(1, 100)
    tries = level()

    for i in range(tries):
        print(f"You have {tries-i} attempts remaining to guess the number")
        while True:
            try:
                guess = int(input(f"Make a guess: "))
                break
            except Exception as e:
                print("Not a ")
                continue

        if guess > number:
            print("Too high.")
        elif guess < number:
            print("Too low.")
        else:
            sys.exit("Guessed correctly!")

        if i == tries - 1:
            sys.exit(f"You've run out guesses, you lose. The correct number was {number}")

        print("Try again.")


def level():
    while True:
        play = input(f"Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if play == 'easy':
            return 10
        elif play == 'hard':
            return 5
        else:
            print("Not a valid response.")


if __name__ == "__main__":
    main()