# body mas index claculator
def BMI(weight_in_kilo, height_in_metre):
    BMICalc = float(weight_in_kilo)/float(height_in_metre) ** 2
    BMI = int(BMICalc)
    if BMI <  18.5:
        print("you are Under weight")
    elif BMI > 18.5 and BMI < 25:
        print("you are normal weight")

    elif BMI > 25 and BMI < 30:
        print("you are over weight")

    elif BMI > 30 and BMI < 35:
        print("you are obese")

    else:
        print("you are clinically obese")

    pass
    print(int(BMI))

def your_life_in_week(age):
    left_age = 90 - int(age)
    days_left = left_age * 365
    months_left = left_age * 12
    weeks_left = left_age * 36

    return f"you have {days_left} days, {weeks_left} weeks and {months_left} months"





command = input("please Provide 0 for BMI and 1 for days in your life ")

if command == "0":
    weight_in_kilo = input("Please Ensert your actual weight ")
    height_in_metre = input("please Ensert your height in metre ")
    BMI(weight_in_kilo = weight_in_kilo, height_in_metre = height_in_metre)


elif command == "1":
    age = input("please ensert your age")
    life = your_life_in_week(age = age)
    print(life)



