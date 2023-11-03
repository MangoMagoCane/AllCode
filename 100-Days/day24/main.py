#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = "[name]"

def main():
    with open("./Input/Names/invited_names.txt", "r") as file:
        names = file.readlines()
    with open("./Input/Letters/starting_letter.txt", "r") as file:
        base_letter = file.read()

    for curr_name in names:
        curr_name = curr_name.strip()
        with open(f"./Output/ReadyToSend/letter_for_{curr_name}.txt", "w") as personalized_letter:
            personalized_letter.write(base_letter.replace(PLACEHOLDER, curr_name))
            

if __name__ == "__main__":
    main()