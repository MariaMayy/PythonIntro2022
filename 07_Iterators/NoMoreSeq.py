def nomore(sequence):
    for seq in sequence:
        for i in sequence:
            if i <= seq:
                yield i