curList = []
bOK = 1
u = 0
d = 0
r = 0
l = 0
s = input()

while (s):
	c = s.split()
	curTuple = (int(c[0]),int(c[1]),int(c[2]),int(c[3]),c[4])
	curList.insert(0, curTuple)

	if ((curTuple[2] == 0) or (curTuple[3] == 0)):
		s = input()
		continue
	if bOK:
		l=curTuple[0]
		r=curTuple[0]
		u=curTuple[1]
		d=curTuple[1]
		bOK = 0

	if (curTuple[0] < l):
		l = curTuple[0]
	if (curTuple[0] + curTuple[2] < l):
		l = curTuple[0] + curTuple[2]
	if (curTuple[0] > r):
		r = curTuple[0]
	if (curTuple[0] + curTuple[2] > r):
		r = curTuple[0] + curTuple[2]
	if (curTuple[1] < d):
		d = curTuple[1]
	if (curTuple[1] + curTuple[3] < d):
		d = curTuple[1] + curTuple[3]
	if (curTuple[1] > u):
		u = curTuple[1]
	if (curTuple[1] + curTuple[3] > u):
		u = curTuple[1] + curTuple[3]
	s = input()

result = [['.']*(r - l) for i in range(u - d)]

while len(curList):
	x, y , c, d1, sym = curList.pop()
	if (c < 0):
		x += c
		c =- c
	if (d1 < 0):
		y += d1
		d1 =- d1
	for i in range(d1):
		for j in range(c):
			result[y + i - d][x + j - l] = sym

for i in range(u - d):
	for j in range(r - l):
		print (result[i][j],end='')
	print('')