import types
import inspect

class init(type):
    def __new__(metacls, name, parents, namespace):
        for cur in namespace:
            if isinstance(namespace[cur], types.FunctionType):
                lNameDef = []
                #if isinstance(namespace[cur], types.GenericAlias):
                if namespace[cur].__defaults__ != None:
                    iLen = len(inspect.get_annotations(namespace[cur])) - len(namespace[cur].__defaults__)   
                    lKeys = list(inspect.get_annotations(namespace[cur]).keys())[:iLen]  
                else:
                    iLen = len(inspect.get_annotations(namespace[cur]))
                    lKeys = list(inspect.get_annotations(namespace[cur]).keys())[:iLen]
                for curAnn in lKeys:  
                    try:
                        lNameDef.append(inspect.get_annotations(namespace[cur])[curAnn]())
                    except:
                        lNameDef.append(None) 
    
                if namespace[cur].__defaults__ == None:
                    namespace[cur].__defaults__ = tuple(lNameDef)
                else:
                    namespace[cur].__defaults__ = tuple(lNameDef) + namespace[cur].__defaults__
        return super().__new__(metacls, name, parents, namespace)

