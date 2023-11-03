import time

def main():
    map0 = {
        3: 'Fizz',
        5: 'Buzz'
    }

    map1 = {
        3: 'Fizz',
        5: 'Buzz',
        7: 'pop',
        11: 'crackle',
        13: 'snap',
        17: 'jounce'
    }


    start = time.time()
    fizz_buzz(100, map0)
    end = time.time()
    run0 = (f"{(end - start) * 1000:.2f} ms")

    start = time.time()
    fizz_buzz(100, map1)
    end = time.time()
    run1 = (f"{(end - start) * 1000:.2f} ms")

    print(f"{run0} {run1}")


def fizz_buzz(max, map):
    for i in range(1, max+1):
        printIndex = True

        for key in map:
            if i % key == 0:
                printIndex = False
                print(map[key], end="")

        print() if printIndex == False else print(i) 


if __name__ == "__main__":
    main()