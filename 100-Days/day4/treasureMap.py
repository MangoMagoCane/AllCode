MAPSIZE = 3

def main():
    map = []
    for _ in range(MAPSIZE):
        map.append([" ", " ", " "])

    position = input("Hiding your treasure! X marks the spot.\n").upper()
    numberList = ord(position[0]) - 65
    letterList = ord(position[1]) - 49 
    map[numberList][letterList] = "X"

    for i in range(MAPSIZE):
        print(map[i])


if __name__ == "__main__":
    main()