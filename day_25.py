
N = 20201227

card_pub = 17115212
door_pub =  3667832

subject_nr = 7


def transform(x, y, N):
    """ Calculates x ** y (mod N)"""
    acc = 1
    while y:
        if y % 2:
            acc = (acc * x) % N
        x = (x * x) % N
        y = y // 2
    return acc

def stupid_log(base, value, N):
    """ Calculates log_{base} value (mod N)"""
    acc = 1
    i = 0
    while acc != value:
        acc = (acc * base) % N
        i += 1    
    return i


card_loop = stupid_log(7, card_pub, N)
door_loop = stupid_log(7, door_pub, N)

encryption_key = transform(door_pub, card_loop, N)
assert encryption_key == transform(card_pub, door_loop, N)

print('Task 1:', encryption_key)

