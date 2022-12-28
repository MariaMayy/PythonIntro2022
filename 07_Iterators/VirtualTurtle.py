def turtle(coord, direction):
    x, y = coord
    curCommand = yield None
    
    while True:
        if (curCommand == 'f'):
            if (direction == 0):
                x += 1
            elif (direction == 1):
                y += 1
            elif (direction == 2):
                x -= 1
            else:
                y -= 1
        elif (curCommand == 'r'):
            direction -= 1
            if (direction < 0):
                direction = 3
        else:
            direction += 1
            if (direction > 3):
                direction = 0  
        curCommand = yield (x, y)
