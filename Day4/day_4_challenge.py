row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

map = [row1, row2, row3]

print(f"{row1}\n {row2}\n {row3}")
position = input("where do you want the X to be Placed")
map[int(position[0])][int(position[1]) - 1] = "X"
print(f"{map[0]}\n {map[1]}\n {map[2]}")
