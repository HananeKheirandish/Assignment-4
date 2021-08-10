import math

def quadratic_equation(a , b , c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("Modele javab nadarad! ")
    elif delta == 0:
        x = -b + math.sqrt(delta)
        print("Rishe haghighi moadele: " , x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Modele 2 rishe haghighi darad : " , x1 , ',' , x2)

a = int(input("please enter a: "))
b = int(input("please enter b: "))
c = int(input("please enter c: "))
quadratic_equation(a , b , c)