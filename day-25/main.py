
# import csv
#
# with open("226 weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
# import pandas as pd
# data = pd.read_csv("226 weather-data.csv")
#
# # convert the hole dataframe in to python dictionary
# data_dict = data.to_dict()
# print(data_dict)


# temp_list = data["temp"].to_list()
# average = sum(temp_list)/len(temp_list)
#
# print(data["temp"].mean())
# print(data["temp"].max())
# condition = data["condition"].to_list()
import pandas as pd
data = pd.read_csv("228201~1.CSV")
list_of_colors = data["Primary Fur Color"].to_list()
print(type(list_of_colors))
# gray_count = 0
# cinnamon_count = 0
# nan_count = 0
# for colors in list_of_colors:
#     if colors == "Gray":
#         gray_count += 1
#     if colors == "Cinnamon":
#         cinnamon_count += 1
#     if colors == "Black":
#         nan_count += 1
gray_squirrel = data[data["Primary Fur Color"] == "Gray"]["Primary Fur Color"].count()
cinnamon_squirrel = data[data["Primary Fur Color"] == "Cinnamon"]["Primary Fur Color"].count()
black_squirrel = data[data["Primary Fur Color"] == "Black"]["Primary Fur Color"].count()
data_dict = {
    "colors": ["Gray", "Cinnamon", "Black"],
    "Counts": [gray_squirrel, cinnamon_squirrel, black_squirrel]
}
data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")

