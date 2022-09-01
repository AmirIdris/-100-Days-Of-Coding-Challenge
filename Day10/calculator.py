

is_finished = False
def multiplication(number1, number2):
    return number1 * number2

def addition(number1, number2):
    return number1 + number2

def substraction(number1, number2):
    return number1 - number2

def division(number1, number2):
    return number1 / number2



operations = {
    "+": addition,
    "*":multiplication,
    "-":substraction,
    "/":division
}




is_finished = False

while not is_finished:
    num1 = int(input("What is The First Number?: "))
    
    
    for operatin in operations:
        print(operatin)
    
    pick_operation = input("Pick Your Operation from the above four Operations: ")

    num2 = int(input("What is The Next Number?: "))

    call_function = operations[pick_operation]
    answer = call_function(number1 = num1, number2 = num2 )
    
    print(f"{num1} {pick_operation} {num2} = {answer}")

    command = input(f"Type 'y' to continues calculating with {answer}, or type 'n' to exit ")

    if command == 'y':
        while command == 'y':

            for operatin in operations:
                print(operatin)
            pick_operation = input("Pick Your Operation from the above four Operations: ")
            num2 = int(input("What is The Next Number?: "))
            call_function = operations[pick_operation]
            answer = call_function(number1 = answer, number2 = num2 )
            print(f"{num1} {pick_operation} {num2} = {answer}")
    
            command = input(f"Type 'y' to continues calculating with {answer}, or type 'n' to exit ")


    elif command == 'no':

        num1 = int(input("What is The First Number?: "))
        
        
        for operatin in operations:
            print(operatin)

        
        pick_operation = input("Pick Your Operation from the above four Operations: ")

    
        num2 = int(input("What is The Next Number?: "))


        call_function = operations[pick_operation]

        answer = call_function(number1 = num1, number2 = num2 )


        print(f"{num1} {pick_operation} {num2} = {answer}")

        command = input(f"Type 'y' to continues calculating with {answer}, or type 'n' to exit ")

    else:
        is_finished = True






    









