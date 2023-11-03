def main():
    name1, name2 = input(), input()
    combinedName = (name1 + name2).lower()
    scoreWords = [["t", "r", "u", "e"], ["l", "o", "v", "e"]]
    loveScore = 0

    for char in combinedName:
        if char in scoreWords[0]:
            loveScore += 10
        if char in scoreWords[1]:
            loveScore += 1

    print(f"Your score is {loveScore}", end="")

    if loveScore < 10 or loveScore > 90:
        print(", you go together like coke and mentos")
    elif loveScore > 40 and loveScore < 50:
        print(", you are alright together.")


if __name__ == "__main__":
    main()