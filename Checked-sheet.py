def checked(x , y):
    for i in range(1, x+1):
        for j in range(1 , y+1):
            if (i+j) % 2 == 0:
                print('#', end='')
            else:
                print('*', end='')
        print( )

num1 = int(input("please enter number1: "))
num2 = int(input("please enter number2: "))
checked(num1 , num2)