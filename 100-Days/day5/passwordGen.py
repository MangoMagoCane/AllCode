import random

def main():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    print("Welcome to the PyPassword Generator!")
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    nr = [nr_letters, nr_symbols, nr_numbers]
    chars = [letters, symbols, numbers]
    nr_used = [0, 0, 0]
    password = ''

    for _ in range(nr_letters + nr_symbols + nr_numbers):
        while True:
            cur_nr_type = random.randint(0, 2)
            cur_amount = nr[cur_nr_type]
            cur_char = chars[cur_nr_type]

            if nr_used[cur_nr_type] < cur_amount:
                break

        nr_used[cur_nr_type] += 1
        password += (cur_char[random.randint(0, len(cur_char) - 1)])

    print(password)
    # print(nr_used)
    

if __name__ == "__main__":
    main()