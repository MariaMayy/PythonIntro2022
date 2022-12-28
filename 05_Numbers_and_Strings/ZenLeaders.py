import time
def sort_key(row):
    return [row[0], row[1][1], row[1][0], row[1][2]]
str = input().split()
curList = []

while str:
    curList.append([time.strptime(str[-1], "%H:%M:%S"), [str[0], str[1], ' '.join(str[2:len(str) - 1]), str[-1]]])
    str = input().split()

curList.sort(reverse = False, key = sort_key)

res = [curList[0][1]]
iCount = 0
idx = 0

while ((iCount < 3) and (idx < (len(curList) - 1))):
    idx += 1
    if (curList[idx][0] != curList[idx - 1][0]):
            iCount += 1
    if (iCount < 3):
        res.append(curList[idx][1])
    

lenMax = [0] * len(res[0])
for cur in res:
    for i in range(len(cur)):
        if len(cur[i]) > lenMax[i]:
            lenMax[i] = len(cur[i])

for cur in res:
        for i in range(len(cur)):
            print('{:<{prec}}'.format(cur[i], prec = lenMax[i]), end=' ')
        print()