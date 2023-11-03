import pandas

def main():
    data = pandas.read_csv("weather_data.csv")
    data_dict = data.to_dict()
    temp_list = data["temp"].to_list()

    avg_temp = 0
    for temp in temp_list:
        avg_temp += temp

    print(data["temp"].max())
    print(data[data.temp == data["temp"].max()])

    monday = data[data.day == "monday"]
    print(monday.condition)




if __name__ == "__main__":
    main()