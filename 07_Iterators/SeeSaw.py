from itertools import chain, filterfalse, tee, zip_longest

def seesaw(sequence):
    t1, t2 = tee(sequence, 2)
    odd_t1 = filterfalse(lambda x: x % 2, t1)
    even_t2 = filterfalse(lambda x: not x % 2, t2)
    
    for i in zip_longest(odd_t1,even_t2):
        for elem in i:
            if (elem != None):
                yield elem
   
#print(*seesaw(i//3 for i in range(1, 27, 2)))
