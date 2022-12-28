import math
a, b, c = eval(input())

if (a == 0):
    if (b == 0):
        print('-1')
    else: print(-c / b)
else:
    D = b**2 - 4*a*c
    if (D < 0):
        print('0')
    elif (D == 0):
        print(- b / (2*a))
    elif (((-b - math.sqrt(D))/(2*a))) < ((-b + math.sqrt(D))/(2*a)):
        print((-b - math.sqrt(D))/(2*a), end=" ")
        print((-b + math.sqrt(D))/(2*a))
    else:
        print((-b + math.sqrt(D))/(2*a), end=" ")
        print((-b - math.sqrt(D))/(2*a))