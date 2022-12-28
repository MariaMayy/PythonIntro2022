class NegExt:
    def __neg__(self):
        try:
            lClass = self.__class__.mro()
            neglClass = lClass[2].__neg__(self)
            
            return self.__class__(neglClass)
        except:
            try:
                curSec = self[1:-1]

                return self.__class__(curSec)
            except:
                return self.__class__(self)
