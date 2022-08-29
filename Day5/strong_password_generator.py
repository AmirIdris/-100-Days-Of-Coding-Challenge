import random
import string

number_of_letters = input("Please input the number of Letter your password will contain ")
number_of_digits = input("please how many digits you requir? ")
number_of_symbol = input("please provide the number of symbols your password have to include")

# letters, digits and symbol used to constract the password
letters = string.ascii_lowercase + string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

password_list = []
# loop through the generated list of charachter, numbers and symbols and pich it randomly
for char in range(0, int(number_of_letters)):
    password_list.append(random.choice(letters))

for num in range(0,int(number_of_digits)):
    password_list.append(random.choice(numbers))

for symbol in range(0, int(number_of_symbol)):
    password_list.append(random.choice(symbols))

# make random order of char, numbers and symbol in the list
random.shuffle(password_list)

# convert the list to strings
password = ""
for i in password_list:
    password = password + i
print(f"Your password is: {password} Keep it Safe")
