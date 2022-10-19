# possible Errors tha could happen in Our Codes

# FileNotFound Error
# with open("data.txt") as file:
#  file.read()

# KeyError
# new_dict ={"key":"value"}
# new_dict["key_value"]

# IndexError
# new_list = ["Amir", "Edris", "Ahimed"]
# new_list[3]

# TypeError
# text = 'abc'
# print(text + 5)
# formula for catching an exception is
# try:
#     something that may through an exception

# except:
# Do this if there is was exception

# else:
# Do this if there was not an exception every thin goes well

# finally:
# Do this No matter what happen
#  FileNotFound Exception and Cathing morethan One Exception

# try:
#     file = open("a_text.txt")
#     new_dict = {"key":"value"}
#     print(new_dict["key"])
# except FileNotFoundError:
#     file = open("a_text.txt", "w")
#     file.write("Write Something")
# except KeyError as error_message:
#     print(f"{error_message} is not found in the key")
#
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError("This is my made up error")
#

height = float(input("provide The height"))
weight = int(input("Provide The weight"))

if height > 3:
    raise ValueError("Human height cannot be more than 3m")
bmi = height + weight
print(bmi)





















