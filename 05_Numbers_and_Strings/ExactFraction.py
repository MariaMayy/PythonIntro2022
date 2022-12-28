from fractions import Fraction
s = input()

newStr = ""
iNum = ""
bOK = False
for cur in s:
   # print("check: ", cur)
   # print(bOK)
    if (cur.isdigit() or cur == '.'):
        iNum += cur
        bOK = True
    elif (not bOK):
        newStr += cur
        bOK = False
    else:
        newStr += "Fraction('" + iNum +"')" + cur
        bOK = False
        iNum = ""
    #if (bOK and (not cur.isdigit() and cur != '.')):
       # newStr += cur
        #bOK = False
 #  print("NewStr: ", newStr)
   # print("CurNum:", iNum)

if (iNum != ""):
    newStr += "Fraction('" + iNum +"')"
        
#print(Fraction('.186'))
#print(newStr)
res = eval(newStr)
print(res)
