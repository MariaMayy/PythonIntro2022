from re import *

curDict = dict()
str = input()

while str:
    str = str.replace(' ', '')
    if (str[0] == '#'):
        str = input()
        continue

    if (findall('[^A-Za-z_][0-9]+E[-+]', str)):
        print("Syntax error")
        str = input()
        continue

    if (('.' in str) or (str.find('**') >= 0) or (str.find('int') >= 0) or (str.find('//') >= 0)):
        print("Syntax error")
        str = input()
        continue

    if ('/' in str):
        str = sub('/', '//', str)

    str = sub(r'([A-Za-z_]+[A-Za-z_0-9]*)', r'_c_\1', str)

    if ('=' in str):
        mname = search('(.*?)=', str)
        name = mname.groups()[0]

        if (not findall('[A-Za-z_]+[A-Za-z_0-9]*', name)):
            print('Assignment error')
            str = input()
            continue

        idx = str.index('=')

        try:
            curDict[name] = eval(str[idx + 1:], None, curDict)

        except NameError:
            print('Name error')
            str = input()
            continue

        except SyntaxError:
            print('Syntax error')
            str = input()
            continue
        
        except TypeError:
            print('Syntax error')
            str = input()
            continue
        
        except:
            print('Runtime error')
            str = input()
            continue
    else:
        try:
            print(eval(str, None, curDict))
            
        except NameError:
            print('Name error')
        except SyntaxError:
            print('Syntax error')
        except TypeError:
            print('Syntax error')
        except:
            print('Runtime error')

    str = input()