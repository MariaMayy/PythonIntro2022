from decimal import Decimal, getcontext
from math import factorial

def PiGen():
    getcontext().prec = 10000
    
    k = 0
    sum = Decimal('0')
    chisl = Decimal('426880')
    chislSqrt = Decimal('10005').sqrt()
    chisl_Pi = 13591409
    znam_Pi = 1

    while True:
        curVal = Decimal(factorial(6*k) * chisl_Pi) / (Decimal(factorial(3*k) * (factorial(k)**3)) * znam_Pi)
        sum += curVal
        curRes = (chisl * chislSqrt) / sum

        yield curRes

        k += 1
        chisl_Pi += 545140134
        znam_Pi *= -262537412640768000


    