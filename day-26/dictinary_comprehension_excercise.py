# dictionary comprehension Exercise
sentence = "What is the Airspeed Velocity of Unladen Swallow"

words = sentence.split(" ")
new_dict = {new_key:len(new_key) for new_key in words}
print(new_dict)