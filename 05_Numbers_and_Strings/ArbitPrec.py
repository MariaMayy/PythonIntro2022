from decimal import Decimal, getcontext

def GetVal(fun, x):
    f = eval(fun)
    return f

result = input()
D = int(input())

getcontext().prec = D + 2

left = Decimal('-1.5')
right = Decimal('1.5')
zero = Decimal('0')

left_Y = GetVal(result, left)
right_Y = GetVal(result, right)

while (right_Y != zero and ((right - left) > 10**(-D))):
    mid = (left + right) / 2
    mid_Y = GetVal(result, mid)

    if ((mid_Y > 0 and left_Y > 0) or (mid_Y < 0 and left_Y < 0)):
        left = mid
        left_Y = mid_Y
    else:
        right = mid
        right_Y = mid_Y

print('{:.{prec}f}'.format(right, prec = D))