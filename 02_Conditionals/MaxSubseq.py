iNum = int(input())
iMaxLen = 0
iLen = 1

while (iNum != 0):
    iNumNext = int(input())
    if (iNumNext >= iNum):
        iLen = iLen + 1
    else:
        if (iLen > iMaxLen):
            iMaxLen = iLen
        iLen = 1
        
    iNum = iNumNext

print(iMaxLen)

    
    


    
