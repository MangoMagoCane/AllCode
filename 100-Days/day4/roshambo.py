import random
import roshambo_art

def main():
    while True:
        try:
            playerMove = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
            if playerMove > 2 or playerMove < 0:
                raise Exception()
            break
        except Exception as e:
            print("Invalid response, try again")

    pcMove = random.randint(0, 2)

    print(roshambo_art.art[playerMove])
    print(f"Computer Chose:\n {roshambo_art.art[pcMove]}")

    if pcMove == playerMove:
        print("Tied")
    elif (playerMove == 0 and pcMove == 2) or (playerMove > pcMove):
        print("You win")
    else:
        print("You Lose")


if __name__ == "__main__":
    main()