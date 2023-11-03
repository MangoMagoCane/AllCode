import pandas

def main():
    data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
    squirrel_colors = {}

    for color in data["Primary Fur Color"]:
        if color not in squirrel_colors:
            squirrel_colors.update({color: 1})
        else:
            squirrel_colors[color] += 1

    data_dict = {
        "Fur Color": list(squirrel_colors),
        "Count": list(squirrel_colors.values())
    }
    
    df = pandas.DataFrame(data_dict)
    df.to_csv("squirrel_count.csv")


if __name__ == "__main__":
    main()