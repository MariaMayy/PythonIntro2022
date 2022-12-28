first = input().split(',')
n = len(first)
matrix = [first]
for _ in range(n - 1):
    matrix.append(input().split(','))

for i in range(0, n):
    for j in range(0, i+1):
        if (j != i+1 and i != 0): 
            print(matrix[i][j], end = ',')
        else: 
            print(matrix[i][j], end = '')
    for k in range(i, 0, -1):
        if (k != 1):
            print(matrix[k-1][i], end = ',')
        else:
             print(matrix[k-1][i], end = '')
    print()
