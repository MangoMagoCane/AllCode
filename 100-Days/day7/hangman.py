import random
import sys
import hangman_art

def main():
    word_list = ["aardvark", "baboon", "camel"]
    word = word_list[random.randint(0, len(word_list)-1)]
    
    lives = 7
    word_length = len(word)

    letters_guessed = ["_"] * word_length
    num_letters_guessed = 0

    while True:
        guess = input("Guess a letter: ")

        successful_guess = False
        while_continue = False

        for i in range(word_length):
            if guess == word[i]:
                if letters_guessed[i] != word[i]:
                    letters_guessed[i] = word[i]
                    num_letters_guessed += 1
                else:
                    print("You've already guessed this letter.")
                    while_continue = True
                    break
        
                successful_guess = True
        
        if while_continue:
            continue
        if successful_guess == False:
            lives -= 1

        print(f"{' '.join(letters_guessed)}  Lives: {lives}")
        print(hangman_art.stages[lives-1])
        
        if lives <= 0:
            sys.exit("You lost the Game.")
        if num_letters_guessed == word_length:
            sys.exit("You Won!")


if __name__ == "__main__":
    main()