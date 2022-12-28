from re import *
from collections import deque
from time import time

start = time()
bCheck = True
str = input()
lClass = list()
dLiner = dict()

while str:
    curTime = time()
    if ((curTime - start) >= 4):
        bCheck = True
        break

    if ((len(str) > 5) and bCheck):
        if (str[0:5] == "class"):
            if ("(" in str):
                lClass = findall("class (.*)[(].*[)]:", str)
                lPar = findall("(?<=[(]).*(?=[)])", str)[0].split(', ')
            else:
                lClass = findall("class (.*):", str)
                lPar = ['']

            if lPar[0] == '':
                dLiner[lClass[0]] = lClass.copy()
            else:
                cur = list()
                cur.append(lClass[0])
                merge_list = list()

                for p in lPar:
                    merge_list.append(dLiner[p].copy())

                sCount = set()
                sCount = sCount.union(*merge_list)

                for _ in range(len(sCount)):
                    if (not bCheck): 
                        break
                    if (not any(merge_list)): 
                        break

                    for curElem in merge_list:
                        if (len(curElem) == 0): 
                            continue

                        current = curElem[0]

                        for i in range(len(merge_list)):
                            if (current in merge_list[i][1:]):
                                bCheck = False
                                break

                            if ((len(merge_list[i]) != 0) and (current == merge_list[i][0])):
                                merge_list[i].pop(0)

                        if bCheck:
                            cur.append(current)
                        break
                dLiner[lClass[0]] = cur.copy()

    str = input()

if bCheck:
    print("Yes")
else:
    print("No")