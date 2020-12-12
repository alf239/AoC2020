
def read_all(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f]

cmds = read_all('input_12')

ds = {
 'E' : (1, 0),
 'S': (0, 1),
 'W': (-1, 0), 
 'N': (0, -1)
}


def move(x, y, dir, v):
    dx, dy = ds[dir]
    x = x + v * dx
    y = y + v * dy
    return x, y


def turn(d, dd):
    return (d + dd // 90 + len(ds)) % len(ds)


d = 0
dns = 'ESWN'
x = 0
y = 0
# print(x, y, dns[d])
for cmd in cmds:
    c = cmd[0]
    v = int(cmd[1:])
    if c == 'R':
        d = turn(d, v)
    elif c == 'L':
        d = turn(d, -v)
    elif c == 'F':
        x, y = move(x, y, dns[d], v)
    else:       
        x, y = move(x, y, c, v)
    # print(cmd, '->', x, y, dns[d])
    print(f'{x}\t{y}\t{dns[d]}')

print()
print(abs(x) + abs(y))