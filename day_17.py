x = """#...#.#.
..#.#.##
..#..#..
.....###
...#.#.#
#.#.##..
#####...
.#.#.##."""

# x = """.#.
# ..#
# ###"""

map = set()
for y, line in enumerate(x.split('\n')):
	for x, c in enumerate(line):
		if c == '#':
			map.add((x, y, 0, 0))

print(map)

deltas = range(-1, 2)
neighbourhood = [(dx, dy, dz, dw) for dx in deltas for dy in deltas for dz in deltas for dw in deltas]
neighbours = [p for p in neighbourhood if p != (0, 0, 0, 0)]

def step(map):
	work = set()
	for x, y, z, w in map:
		deltas = range(-1, 2)
		work.update([(x + dx, y + dy, z + dz, w + dw) for dx, dy, dz, dw in neighbourhood])
	map1 = set()
	for x, y, z, w in work:
		occupancy = sum([1 for dx, dy, dz, dw in neighbours if (x + dx, y + dy, z + dz, w + dw) in map])
		# print(f'{(x, y, z)} = {occupancy}')
		if occupancy == 3 or (occupancy == 2 and (x, y, z, w) in map):
			map1.add((x, y, z, w))
	return map1

def print_map(map):
	pass
	# zs = sorted([t for t in set([z for x, y, z in map])])
	# ys = set([y for x, y, z in map])
	# xs = set([x for x, y, z in map])
	# for z in zs:
	# 	print(f'z = {z}')
	# 	for y in range(min(ys), max(ys)+1):
	# 		for x in range(min(xs), max(xs)+1):
	# 			print('#' if (x, y, z) in map else '.', end = '')
	# 		print()
	# 	print('\n')


print_map(map)
for i in range(6):
	map = step(map)
	print_map(map)

print(len(map))