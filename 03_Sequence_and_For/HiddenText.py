import string

StrMain = input()
StrFind = input()
iLen = len(StrFind)
iLenMain = len(StrMain)
bOK = False

while (StrMain.count(StrFind[0]) != 0):
    if (iLen == 0):
        break
    elif (iLen == 1):
        if (StrFind in StrMain):
            bOK = True
        else:
            break
    else:
        IndexFirst = StrMain.find(StrFind[0])
        IndexSecond = StrMain.find(StrFind[1])
        
        if (IndexSecond == (iLenMain - 1)):
            bOK = True
        else:    
            if ((IndexSecond != -1) and (IndexFirst != -1)):
                iUp = IndexSecond - IndexFirst
                for i in StrFind[2:]:
                    if ((iLenMain + 1) > IndexSecond + iUp):
                        if StrMain[IndexSecond + iUp] == i:
                            bOK = True
                            IndexSecond = IndexSecond + iUp 
                        else:
                            bOK = False
                            break
                    else:
                        bOK = False
                        break
    if bOK:
        break
    else:
        if StrMain.find(StrFind[0]) == -1:
            break
        else:
            StrMain = StrMain[StrMain.find(StrFind[0])+1:]
if bOK:
    print('YES')
else:
    print('NO')