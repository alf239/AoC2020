from dataclasses import dataclass
from typing import List
from functools import reduce

@dataclass
class Tile:
    id: int
    nwse1: List[int]
    nwse2: List[int]
    body: List[str]


def read_all(filename):
    with open(filename) as f:
        return [line.strip() for line in f]


x = read_all('input_20')

tiles = []
id = -1
n = None
w = None
s = None
e = None
n1 = None
w1 = None
s1 = None
e1 = None
body = []

for l in x:
    # print(l)
    if l.startswith('Tile '):
        id = int(l[5:-1])
        left = ''
        right = ''
        body = []
    elif l == '':
        id = None
    else:  # tile line
        if left == '':  # North
            top = l.replace('.', '0').replace('#', '1')
            n = int(top, 2)
            n1 = int(top[::-1], 2)
        
        left += '0' if l[0] == '.' else '1'
        right += '0' if l[-1] == '.' else '1'
        body.append(l)

        if len(left) == 10:
            e1 = int(left, 2)
            e = int(left[::-1], 2)
            w = int(right, 2)
            w1 = int(right[::-1], 2)
            btm = l.replace('.', '0').replace('#', '1')
            s1 = int(btm, 2)
            s = int(btm[::-1], 2)
            tiles.append(Tile(id, [n, e, s, w], [n1, e1, s1, w1], body))

size = {}
for t in tiles:
    for k in t.nwse1:
        n = size.get(k, 0)
        size[k] = n + 1
    for k in t.nwse2:
        n = size.get(k, 0)
        size[k] = n + 1

singletons = set(k for k, v in size.items() if v == 1)

corners = []
for t in tiles:
    if len([s for s in t.nwse1 if s in singletons]) == 2:
        corners.append(t)

res = 1
for c in corners:
    res *= c.id
print('Task 1:', res)


monster = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """

monster_mask = [(x, y) for y, l in enumerate(monster.split('\n'))
                        for x, c in enumerate(l)
                        if c == '#']

def is_monster(x, y, m):
    for dx, dy in monster_mask:
        if m[y + dy][x + dx] != '#':
            return False
    return True


def full_map(tiles):
    

print(corners[0])
 