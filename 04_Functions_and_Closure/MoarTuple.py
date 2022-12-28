def moar(a, b, n):
    iCountA, iCountB = 0, 0
    for i in range(len(a)):
        if (a[i] % n == 0):
            iCountA += 1
    for i in range(len(b)):
        if (b[i] % n == 0):
            iCountB += 1
    if (iCountA > iCountB): 
        return True
    else:
        return False

#print(moar((25,0,-115,976,100500,7),(32,5,78,98,10,9,42),5))    
print(type(range(-2, 10)))