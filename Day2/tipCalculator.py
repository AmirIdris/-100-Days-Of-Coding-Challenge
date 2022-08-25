print("Welcome to tip calculator \n")

bill_amount = input("what was the total bill? ")
percentage_tip = input("what percentage tip would you like to give ? 10, 12 or 15 ?")
people = input("How many people would you like to split ?")
payment = (int(bill_amount)/int(people))*(int(percentage_tip)/100)

print(round(payment,3))