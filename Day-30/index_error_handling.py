fruits = ["apple", "orange", "pear"]

# question
# def make_pie(index):
#     fruit = fruits[index]
#     print(fruit + "pie")
#
# make_pie(4)

def make_pie(index):
    try:
        fruit = fruits[index]

    except:
        print("Fruit Pie")
    else:
        print(fruit + " pie")


make_pie(2)