k = int(input())
 
iNum = 0
p = 10

while ((k*(p//10) + iNum) != ((iNum*10 + k)*k)):
    iNum = (iNum*10 + k)*k % p 
    p = p * 10
 
print(iNum*10 + k)