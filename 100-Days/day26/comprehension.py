

def main():
    # name = "Val"
    # name_list = [letter for letter in name]

    # print(name_list)

    # num_list = [num * 2 for num in range(1,5) if num % 2]
    # print(num_list)

    # names = ["Alex", "Beth", "Caroline", "Dave", "Freddie", "Eleanor"]
    # long_names = [name.upper() for name in names if len(name) > 4]
    # print(long_names)

    # numbers = [1, 1, 2, 4, 9, 18, 6, 3]
    # squared_numbers = [num * num for num in numbers]
    # print(squared_numbers)

    # list_of_strings = ["1", "4", "6", "7", "33", "40", "59"]
    # even_numbers = [int(num) for num in list_of_strings if int(num)%2==0]
    # print(list_of_strings, even_numbers)

    # with open("file1.txt") as file:
    #     list_1 = [int(num) for num in file.readlines()]
    # with open("file2.txt") as file:
    #     list_2 = [int(num) for num in file.readlines()]
    # results = [num for num in list_1 if num in list_2]
    # print(results)

    # text = "What is the Airspeed Velocity of an Unladen Swallow?"
    # result = {word:len(word) for word in text.split(" ")}
    # print(result)

    weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
    weather_f = {day:temp * 9/5 + 32 for (day,temp) in weather_c.items()}
    print(weather_f)






if __name__ == "__main__":
    main()