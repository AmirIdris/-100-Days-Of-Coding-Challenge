print("Welcome to python Pizza Deliverries ")
size = input("What Size of Pizza Do you want? S, M, or L ")
add_pepperoni = input("Do You want Pepperoni? Y or N ")
extra_cheese = input("Do You want Extra Cheese Y or N ")

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2

    if extra_cheese == "Y":
        bill += 1


elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3

    if extra_cheese == "Y":
        bill += 1
else:
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
print(f"${bill}")