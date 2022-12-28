from math import *
def maxfun(*args):
    bCheck = True
    idxMax = 1
    
    for j in range(1, len(args)):
        iSum = 0
        for k in args[0]:
            iSum += (args[j])(k)
        if (bCheck):
            bCheck = False
            iPrevSum = iSum
        elif (iSum >= iPrevSum):
            iPrevSum = iSum
            idxMax = j
       
    return args[idxMax]
    
#print(maxfun(range(-2,10), sin, cos, exp)(1))
#print(maxfun([x/10000 for x in range(-100000, 10000)] , lambda x: x**2, lambda x: x**3, exp)(2))