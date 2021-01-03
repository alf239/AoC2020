from dataclasses import dataclass
from typing import List
from functools import reduce
import itertools

@dataclass
class Tile:
    id: int
    body: List[str]


def north(tile):
    return tile.body[0]


def south(tile):
    return tile.body[-1]


def east(tile):
    return ''.join(r[-1] for r in tile.body)


def west(tile):
    return ''.join(r[0] for r in tile.body)


def flip_we(tile):
    return Tile(tile.id, [line[::-1] for line in tile.body])


def transpose(tile):
    new_body = [''.join(l[i] for l in tile.body) for i in range(len(tile.body[0]))]
    return Tile(tile.id, new_body)


def rotate_cw(tile):
    return flip_we(transpose(tile))
    

def read_all(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()


def tiles_from(lines):
    id = -1
    body = []
    for l in lines:
        if l.startswith('Tile '):
            id = int(l[5:-1])
        elif l == '':
            id = None
            body = []
        else:  # tile line
            body.append(l)
            if len(body) == 10:
                yield Tile(id, body)


def multimap_add(mm, k, v):
    vals = mm.get(k, [])
    vals.append(v)
    mm[k] = vals


x = read_all('input_20')

tiles = [t for t in tiles_from(x)]

index_n = {}
index_w = {}
for t in tiles:
    t1 = t
    t2 = transpose(t)
    for _ in range(4):
        multimap_add(index_n, north(t1), t1)
        multimap_add(index_n, north(t2), t2)
        multimap_add(index_w, west(t1), t1)
        multimap_add(index_w, west(t2), t2)
        t1 = rotate_cw(t1)
        t2 = rotate_cw(t2)

print('Indexes', len(tiles), len(index_n), len(index_w))

sides = [t.id for k, ts in index_n.items() if len(ts) == 1 for t in ts]
corners = [k for k, ts in itertools.groupby(sides) if len(list(ts)) == 4]  # 2 per side, 2 sides

res = 1
for c in corners:
    res *= c
print('*** Task 1:', res, '***')

## And now to monsters

tiles_idx = {}
for _, ts in index_n.items():
    for t in ts:
        multimap_add(tiles_idx, t.id, t)
assert len(tiles_idx) == len(tiles)
assert all(len(ts) == 8 for _, ts in tiles_idx.items())

start_tiles = [t for c in corners 
                 for t in tiles_idx[c]
                 if len(index_n[south(t)]) == 2
                    and len(index_w[east(t)]) == 2]
assert len(start_tiles) == 8  # 4 corners, 2 transpositions


def row(t):
    while t:
        yield t
        next = [tt for tt in index_w[east(t)] if tt.id != t.id]
        t = next[0] if next else None


def column(t):
    while t:
        yield t
        next = [tt for tt in index_n[south(t)] if tt.id != t.id]
        t = next[0] if next else None


def full_sea(t):
    return [list(row(tile)) for tile in column(t)]


def lookup(sea, x, y):
    t = sea[0][0]
    xs = len(t.body[0]) - 2
    ys = len(t.body) - 2
    # print(x, y, xs, ys, x // xs, y // ys, x % xs, y % xs, x % xs + 1, y % ys + 1)
    return sea[y // ys][x // xs].body[y % ys + 1][x % xs + 1]


monster = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """

monster_mask = [(x, y) for y, l in enumerate(monster.split('\n'))
                       for x, c in enumerate(l)
                       if c == '#']


def is_monster(sea, x, y):
    for dx, dy in monster_mask:
        if lookup(sea, x + dx, y + dy) != '#':
            return False
    return True


def width(sea):
    return len(sea[0]) * (len(sea[0][0].body[0]) - 2)


def height(sea):
    return len(sea) * (len(sea[0][0].body) - 2)


def has_monster(sea):
    mx = max(x for x, y in monster_mask)
    my = max(y for x, y in monster_mask)
    for y in range(height(sea) - my):
        for x in range(width(sea) - mx):
            if is_monster(sea, x, y):
                return True
    return False


def print_sea(sea):
    for y in range(height(sea)):
        for x in range(width(sea)):
            print(lookup(sea, x, y), end='')
        print()


good_sea = []
for t in start_tiles:
    sea = full_sea(t)
    if has_monster(sea):
        good_sea.append(sea)

assert len(good_sea) == 1

sea = good_sea[0]
dots = [[]]
for y in range(height(sea)):
    for x in range(width(sea)):
        dots[-1].append(lookup(sea, x, y))
    dots.append([])
dots = dots[:-1]

mx = max(x for x, y in monster_mask)
my = max(y for x, y in monster_mask)
for y in range(height(sea) - my):
    for x in range(width(sea) - mx):
        if is_monster(sea, x, y):
            for dx, dy in monster_mask:
                dots[y+dy][x+dx] = 'o'

# print([''.join(line) for line in dots])
print('*** Task 2:', len([c for line in dots for c in line if c == '#']), '***')
