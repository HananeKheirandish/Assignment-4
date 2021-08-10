def multiplication(x,y):
    for i in range(1 , x+1):
        for j in range(1 , y+1):
            print(i*j , end = '  ')
            if(j == y):
                print( )

num1 = int(input("please enter number1: "))
num2 = int(input("please enter number2: "))
multiplication(num1 , num2)