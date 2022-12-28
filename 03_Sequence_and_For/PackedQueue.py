from collections import deque

sequence = eval(input())
curDeq = deque([])

for cur in sequence:
	if (type(cur) is tuple):
		curDeq.extend(cur)
	elif (len(curDeq) < cur):
		break
	else:
		print(tuple([curDeq.popleft() for i in range(cur)]))
