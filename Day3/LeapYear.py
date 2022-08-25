year = input("Please Enter The Year ")
parsed_year = int(year)
if parsed_year % 4 == 0:
    if parsed_year % 100 == 0 and parsed_year % 400 == 0:
        print("leap")
    else:
        print("Not Leap!")

else:
    print("Not Leap")