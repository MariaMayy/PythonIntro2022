x, y, z = eval(input())
xMin = xMax = x
yMin = yMax = y
zMin = zMax = z
bCheck = True

while (bCheck):
    s = input()
    if s == '':
        bCheck = False
    else:
        bCheck = True
        x, y, z = eval(s)

        if (x > xMax):
            xMax = x
        if (x < xMin):
            xMin = x
        if (y > yMax):
            yMax = y
        if (y < yMin):
            yMin = y
        if (z > zMax):
            zMax = z
        if (z < zMin):
            zMin = z

Vol = abs(xMax - xMin)*abs(yMax - yMin)*abs(zMax - zMin)
print(Vol)