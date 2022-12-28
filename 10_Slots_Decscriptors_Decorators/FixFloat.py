def fix(n):
    def decorator(func):
        def newf(*args, **kwargs):
            Dict = {}
            kDict = {}

            for i in range(len(args)):
                if (isinstance(args[i], float)):
                    cur = round(args[i], n)
                    Dict.update({i:cur})
                else:
                    Dict.update({i:args[i]})

            curTuple = tuple(Dict.values())

            for j, k in kwargs.items():
                if (isinstance(k, float)):
                    kCur = round(k, n)
                    kDict.update({j:kCur})
                else:
                    kDict.update({j:k})
            
            result = func(*curTuple, **kDict)
            if isinstance(result, float):
                return round(result, n)
            else:
                return result

        return newf
    return decorator
