
def read_all(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f]

cmds = read_all('input_12')

def turn(x, y, dd):
    #        2  3    -3  2    -2  -3    3  -2
    return [(x, y), (-y, x), (-x, -y), (y, -x)][(dd // 90 + 4) % 4]


x = 0
y = 0
dx = 10
dy = -1
# print(x, y, dns[d])
for cmd in cmds:
    c = cmd[0]
    v = int(cmd[1:])
    if c == 'R':
        dx, dy = turn(dx, dy, v)
    elif c == 'L':
        dx, dy = turn(dx, dy, -v)
    elif c == 'F':
        x = x + v * dx
        y = y + v * dy
    elif c == 'E':
        dx = dx + v
    elif c == 'W':
        dx = dx - v
    elif c == 'N':
        dy = dy - v
    elif c == 'S':
        dy = dy + v
    else:
        raise "Unknown command"

    # print(cmd, '->', x, y, dns[d])
    print(f'{x}\t{y}\t{dx}\t{dy}')

print()
print(abs(x) + abs(y))