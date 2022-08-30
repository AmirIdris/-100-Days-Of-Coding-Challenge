n= int(input("check this Number: "))

def check_this_number(n):
    divindend = []
    for i in range(1,100):      
        if n%i == 0:
            divindend.append(i)
    if len(divindend) == 2 and divindend[0] ==1 and divindend[1] == n:
        return "it is prime"
    else:
        return "It is not prime"


# function that calculate prime number 
def check_prime(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    if is_prime == True:
        return "It is Prime"
    else:
        return "It is Not Prime"
    

num = check_prime(number = n)
print(num)