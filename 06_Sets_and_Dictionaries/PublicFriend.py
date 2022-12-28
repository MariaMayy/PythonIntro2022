from collections import defaultdict

dFriend = defaultdict(set)
AllFriends = set()
result = []
s = input()
while (s):
    M, N = map(int, s.split(', '))
    if (M == 0 and N == 0):
        break
    dFriend[M].add(N)
    dFriend[N].add(M)
    AllFriends.add(M)
    AllFriends.add(N)
    s = input()

iCountAll = len(AllFriends) - 1

for name, setFriend in dFriend.items():
    curCount = len(setFriend)
    if (iCountAll == curCount):
        result.append(name)

if (len(result) != 0):
    sortRes = sorted(result, reverse=False)
    result.sort()
    for curPlayer in sortRes:
        print(curPlayer, end = ' ')
else:
    print()
