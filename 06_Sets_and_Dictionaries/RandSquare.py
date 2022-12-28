import random

def randsquare(A, B):
    diag = ((abs(A[0] - B[0])**2 + abs(A[1] - B[1])**2)**(1/2))
    side = (diag**2 / 2)**(1/2)
    cosin = abs(A[0] - B[0]) / diag
    sinus = abs(A[1] - B[1]) / diag
    coef = 1 / (2**(1/2))

    if (B[0] < A[0]):
        cosin = - cosin
    if (B[1] < A[1]):
        sinus = - sinus
    
    x0 = random.uniform(0, side)
    y0 = random.uniform(0, side)

    x1 = x0*coef + y0*coef
    y1 = - x0*coef + y0*coef

    xFinal = A[0] + x1 * cosin - y1 * sinus
    yFinal = A[1] + x1 * sinus + y1 * cosin

    return (xFinal, yFinal)
