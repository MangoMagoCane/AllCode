import random

def main():
    names_string = "Angela, Ben, Jenny, Chloe"
    names = names_string.split(", ")

    payer = random.randint(0, len(names)-1)
    print(f"{names[payer]} is going to pay for the meal today!")

if __name__ == "__main__":
    main()