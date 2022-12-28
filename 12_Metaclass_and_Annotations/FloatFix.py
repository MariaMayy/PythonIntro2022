import types
import numbers

class fixed(type):
    def __new__(metacls, name, parents, namespace, ndigits = 3):
        def decorator(func):
            def newf(*args, **kwargs):
                Dict = {}
                kDict = {}

                for i in range(len(args)):
                    if (isinstance(args[i], float)):
                        cur = round(args[i], ndigits)
                        Dict.update({i:cur})
                    else:
                        Dict.update({i:args[i]})

                curTuple = tuple(Dict.values())

                for j, k in kwargs.items():
                    if (isinstance(k, numbers.Real)):
                        kCur = round(k, ndigits)
                        kDict.update({j:kCur})
                    else:
                        kDict.update({j:k})
                
                result = func(*curTuple, **kDict)
                if isinstance(result, numbers.Real):
                    return round(result, ndigits)
                else:
                    return result

            return newf
        for cur in namespace:
            if isinstance(namespace[cur], types.FunctionType):
                namespace[cur] = decorator(namespace[cur])
        return super().__new__(metacls, name, parents, namespace)
