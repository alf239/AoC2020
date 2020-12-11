
def read_all(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f]



def seat(a, x, y):
    if y < 0 or y >= len(a): return 'o'
    if x < 0 or x >= len(a[y]): return 'o'
    return a[y][x]


def occupancy(a, x, y):
    offsets = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1),           (0, 1),
                (1, -1),  (1, 0),  (1, 1)]
    res = 0
    for dx, dy in offsets:
        i = 0
        see = '.'
        while see == '.':
            i = i + 1
            see = seat(a, x + i * dx, y + i * dy)
        if see == '#':
            res = res + 1
    return res


def next_state(a, x, y, st):
    if st == '.': return '.'
    occ = occupancy(a, x, y)
    if st == 'L' and occ == 0: return '#'
    if st == '#' and occ >= 5: return 'L'
    return st


a = read_all('input_11')

N = len(a)
M = len(a[0])

changes = True
while changes:
    print(chr(27) + "[2J")
    print('\n'.join(a[:40]))
    changes = False
    new_a = []
    for i in range(N):
        row = ''
        for j in range(M):
            st = seat(a, j, i)
            new_st = next_state(a, j, i, st)
            if new_st != st: changes = True
            row = row + new_st
        new_a.append(row)
    a = new_a

print(sum([1 for row in a for c in row if c == '#']))

          