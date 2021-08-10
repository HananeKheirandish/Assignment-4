def maghsoom_alaih(x):
    list = []
    for i in range(1,x+1):
        if x % i == 0:
            list.append(i)
    return list

def bmm(x,y):
    maghsoom = []
    for i in maghsoom_alaih(x):
        for j in maghsoom_alaih(y):
            if i == j:
                maghsoom.append(i)
    print("b m m is: " , max(maghsoom))

num1 = int(input("please enter number1: "))
num2 = int(input("please enter number2: "))
bmm(num1,num2)