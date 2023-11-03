import sys

def main():
    print("Welcome to treasure Island.\nYour mission is to find the treasure.")
    state = start1()
    while True:
        state = state()


def start1():
    choice = decision("You are at a cross road. Where do you want to go?", ['left', 'right'])
    if choice == 'right':
        sys.exit("You fall into a hole. Game Over.")
    else:
        return lake2()


def lake2():
    choice = decision("You've come to a lake. There is an island in the middle of the lake. Do you either wait for a boat to come, or swim accross?", ['wait', 'swim'])
    if choice == 'swim':
        sys.exit("You get attacked by an aggressive pike. Game Over.")
    else:
        return island3()


def island3():
    choice = decision("You arrive to the island unharmed. There is a house with three doors, which do you choose?", ['red', 'yellow', 'blue'])
    if choice == 'red':
        sys.exit("You entered a room filled with fire. Game Over.")
    elif choice == 'blue':
        sys.exit("You entered a room that was booby trapped. Game Over.")
    else:
        sys.exit("You entered the room and found the treasure!")


def decision(text, options):
    optionsText = f"\"{options[0]}\""
    for option in options[1:-1]:
        optionsText = optionsText + f", \"{option}\""
    optionsText = optionsText + f" or \"{options[-1]}\""

    while True:
        choice = input(f"{text} \ntype {optionsText} ").lower()
        for option in options:
            if choice == option:
                return option
            
        print("invalid response")


if __name__ == "__main__":
    main()