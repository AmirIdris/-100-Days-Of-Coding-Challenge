import random
# list comprehension Excercise
with open("file1.txt") as number1:
    number1_list = number1.readlines()
    number1.close()
with open("file2.txt") as number2:
    number2_list = number2.readlines()
    number2.close()
# num1_list = []
# for num in number1_list:
#     num1_list.append(num.strip())

first_number_list = [int(num.strip()) for num in number1_list]
second_number_list = [int(num.strip()) for num in number2_list]

result = [num for num in second_number_list if num in first_number_list]
print(result)

# looping through dictionary
student_dict = {
    "student":["angela","amir"],
    "score": [100,80]
}

for (key,value) in student_dict.items():
    print(value)








# list comprehension
# formula for range is
# previous_list = [a,b,c]
# new_list = [new_item for item in previous_list]

double_the_number = [rng*2 for rng in range(1,5)]
print(double_the_number)

# conditional list comprehension
# formula for conditional list comprehension
# new_list = [new_item for item in previous_list if test]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_name = [name for name in names if len(name) == 4]
print(short_name)

# convert to upper case

capitalized_name = [name.upper() for name in names if len(name) > 5]
print(capitalized_name)

# calculate square of those number
numbers = [1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num*num for num in numbers]
print(squared_numbers)
# filter even number using one line of code

given_numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num for num in given_numbers if num % 2 == 0]
print(result)

# Dictionary Comprehension is way of creating nwe dictionary from existing list or dictionary
# formula for dictionary comprehension is using existing list
# new_dict = {new_item:new_value for item in list}
# formula for creating new dictionary from existing dictionary
# new_dict = {new_item:new_value for (key,value) in existing_dictionary.items()}

# example generating new dictionary from existing list
names = ['alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

new_dict = {new_key:random.randint(1,100) for new_key in names}
print(new_dict)

# example creating new_dictionary from existing dictionary

passed_student = {new_key:new_value for (new_key, new_value) in new_dict.items() if new_value >50}
print(passed_student)



























