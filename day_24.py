
def read_all(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f]


def commands(s):
    prev = None
    for c in s:
        if prev:
            yield prev + c
            prev = None
        elif c in 'ew':
            yield c
        else:
            prev = c


def move(q, r, c):
    if c == 'w':
        return q-1, r
    if c == 'e':
        return q+1, r
    if c == 'nw': 
        return q, r-1
    if c == 'ne':
        return q+1, r-1
    if c == 'sw': 
        return q-1, r+1
    if c == 'se':
        return q, r+1
    raise c


def neighbours(q, r):
    for c in ['w', 'e', 'nw', 'ne', 'sw', 'se']:
        yield move(q, r, c)


xs = read_all('input_24')

m = set()
for line in xs:
    q, r = 0, 0
    for c in commands(line):
        q, r = move(q, r, c)
    if (q, r) in m:
        m.remove((q, r))
    else:
        m.add((q, r))

print('Task 1', len(m))


for _ in range(100):
    consider = set(z for q, r in m for z in neighbours(q, r))
    m1 = set()
    for q, r in consider:
        nbrs = len([1 for z in neighbours(q, r) if z in m])
        if (q, r) in m:
            if nbrs in [1, 2]:
                m1.add((q, r))
        else:
            if nbrs == 2:
                m1.add((q, r))
    m = m1


print('Task 2', len(m))
