import sys

def main():
    while True:
        operation = input("Type 'encode' to encrypt or 'decode' to decrypt: ")
        if operation == "decode":
            shift *= -1
        elif operation != "encode":
            sys.exit("Invalid operation")
          
        message = input("Type your message: ")
        shift = int(input("Type the shift number: ")) 

        cipher(operation, message, shift)
        
        if input("Type 'yes' if you want to go again. Otherwise, any character ") != 'yes':
            break
            

def cipher(op, text, shift):
    text.lower()
    shift %= 26
    cipher = ""

    for char in text:
        uni_char = ord(char) + shift
        if not char.isalpha():
            cipher += char
            continue
        elif uni_char > ord("z"):
            uni_char += - ord("z") + ord("a")
        elif uni_char < ord("a"):
            uni_char += - ord("a") + ord("z")
        cipher += chr(uni_char)

    print(f"Here's the {op}d result: {cipher}")


if __name__ == "__main__":
    main()