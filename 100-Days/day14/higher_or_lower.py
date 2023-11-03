import random
import sys
from game_data import data
from art import logo, vs

DATA_COUNT = len(data)

def main():
    score = 0

    print(logo)

    person_a = get_person("")
    person_b = get_person(person_a['name'])

    while True:
        print(f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}")
        print(vs)
        print(f"Compare B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}")

        correct = False
        while True:
            guess = input("Who has more followers? Type 'A' or 'B': ").upper()

            if guess == 'A':
                if person_a['follower_count'] > person_b['follower_count']:
                    correct = True
                    person_b = get_person(person_a['name'])
                break
            elif guess == 'B':
                if person_b['follower_count'] > person_a['follower_count']:
                    correct = True
                break
            else:
                print("Invalid response.")

        person_a = person_b
        person_b = get_person(person_a['name'])
            
        if correct:
            score += 1
            print(f"You're right! Current score: {score}\n\n")
        else:
            sys.exit(f"Sorry, that's wrong. Final score: {score}")



    
def get_person(prev_name: str):
    while True:
        index = random.randint(0, DATA_COUNT-1)
        if index != prev_name:
            return data[index]


if __name__ == "__main__":
    main()