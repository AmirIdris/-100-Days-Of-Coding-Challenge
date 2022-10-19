# unlimited number of arguments
def add(*args):
    return f"Sum Of {args[0]} {args[1]} {args[2]} is: {sum(args)}"


def calculate(**kwargs):
    for (key,value) in kwargs.items():
        print(f"{key}:{value}")

    # return kwargs['sumup'] + kwargs['multiply']


summation = add(10, 20, 30)
calculate(sumup=3, multiply=4)
print(summation)

