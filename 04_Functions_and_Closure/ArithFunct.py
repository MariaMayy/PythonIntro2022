def SUB(arg1, arg2):
    def result(x):
        nonlocal arg1
        nonlocal arg2

        if (callable(arg1)):
            arg1 = arg1(x)
        if (callable(arg2)):
            arg2 = arg2(x)
        return arg1 - arg2
    return result

def ADD(arg1, arg2):
    def result(x):
        nonlocal arg1
        nonlocal arg2

        if (callable(arg1)):
            arg1 = arg1(x)
        if (callable(arg2)):
            arg2 = arg2(x)
        return arg1 + arg2
    return result

def MUL(arg1, arg2):
    def result(x):
        nonlocal arg1
        nonlocal arg2

        if (callable(arg1)):
            arg1 = arg1(x)
        if (callable(arg2)):
            arg2 = arg2(x)
        return arg1 * arg2
    return result

def DIV(arg1, arg2):
    def result(x):
        nonlocal arg1
        nonlocal arg2

        if (callable(arg1)):
            arg1 = arg1(x)
        if (callable(arg2)):
            arg2 = arg2(x)
        return arg1 / arg2
    return result

#from math import *

#f = SUB(sin, cos)
#print(f(12), sin(12)-cos(12))

#g = DIV(sin, cos)
#print(g(pi/6), tan(pi/6))

#h = MUL(exp, 0.1)
#print(h(2), e**2/10)

#t = ADD(len, sum)
#print(t(range(5)))