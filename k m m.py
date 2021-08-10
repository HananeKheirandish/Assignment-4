def mazrab_moshtarak(x):
    list = []
    for i in range(1,100):
        list.append(x * i)
    return list

def kmm(x,y):
    mazrab = []
    for i in mazrab_moshtarak(x):
        for j in mazrab_moshtarak(y):
            if i == j:
                mazrab.append(i)
    print("k m m is: " , min(mazrab))

num1 = int(input("please enter number1: "))
num2 = int(input("please enter number2: "))
kmm(num1,num2)