import math
N = int(input())
count = 0
List = []

x = int(math.sqrt(N)/4)

while (x*x <= N):
    y = int(math.sqrt(N-x*x)/3)
    while (y <= x and x*x + y*y <= N):
        z = int(math.sqrt(N-x*x-y*y)/2)
        while (z <= y and x*x+y*y+z*z <= N):
            if (N-x*x-y*y-z*z <= z*z):
                count += 1
                t = int(math.sqrt(N-x*x-y*y-z*z))
                if(x*x+y*y+z*z+t*t==N):
                    SCur = (x, y, z, t)
                    sorted(SCur)
                    List.append(SCur)
            z += 1
        y += 1
    x += 1

i = 0
for i in range(len(List)):
    print(*List[i])