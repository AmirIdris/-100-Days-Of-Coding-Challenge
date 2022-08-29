# Program that add app all even number from 0 to 100
total = 0
for number in range(2, 101, 2):
    total += number

print(total)

# peogram that mimic fiz buz kid game 

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    elif i % 3 == 0:
        print("Fizz")

    elif i % 5 == 0:
        print("Buzz")

    else:
        print(i)
