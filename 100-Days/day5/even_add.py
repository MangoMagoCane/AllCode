def main():
    largestInt = int(input("Add all even digits from 2 to "))
    evenSum = 0
    
    for num in range(2, largestInt + 1, 2):
        evenSum += num

    print(evenSum)


if __name__ == "__main__":
    main()