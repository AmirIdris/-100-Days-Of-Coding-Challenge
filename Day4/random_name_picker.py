import random
name = input("please Provide Comma separated Names ")
splitted_name = name.split(", ")

selected_name = random.randint(0, len(splitted_name) - 1)
the_person_to_pay = splitted_name[selected_name]

print(f"the person that is going to pay is {the_person_to_pay}")