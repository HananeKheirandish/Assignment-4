import math

def factorial(fact):
    for i in range(fact):
        f = int(math.factorial(i))
        if f == fact:
            t = 1
            break
        else:
            t = 0
    if t==1:
        print("yes.")
    else:
        print("No!")

number = int(input("please enter your number: "))
factorial(number)