print("Welcome To Love Calculator! ")
name1 = input("What is Your Name? \n")
name2 = input("what is Her Name? \n")

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

countTrue = lower_case_name1.count('t') + lower_case_name2.count('t') + lower_case_name1.count('r') + lower_case_name2.count('r') +lower_case_name1.count('u') + lower_case_name2.count('u') + lower_case_name1.count('e') + lower_case_name2.count('e')
countLove = lower_case_name1.count('l') + lower_case_name2.count('l') + lower_case_name1.count('o') + lower_case_name2.count('o') +lower_case_name1.count('v') + lower_case_name2.count('v') + lower_case_name1.count('e') + lower_case_name2.count('e')
score = str(countTrue) + str(countLove)
if int(score) < 100 and int(score) > 90:
    print(f"You are amazing Couple Your Score is {score}")
elif int(score) < 50 and int(score) > 40:
    print(f"your score is {score} You better be togather")

else:
   print(f"your score is {score} You better be separate") 
