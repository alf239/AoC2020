
def read_all(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f]

parts = read_all('input_16')
first_empty = parts.index('')
last_empty = parts.index('', first_empty + 1)

def to_ticket(line):
    return [int(x) for x in line.split(',')]

locs = parts[:first_empty]
assert parts[first_empty+1] == 'your ticket:'
mine = to_ticket(parts[first_empty+2])
assert parts[last_empty+1] == 'nearby tickets:'
tickets = [to_ticket(line) for line in parts[last_empty+2:]] 

print(mine)

valid = set()
for loc in locs:
    details = loc.split(': ')[1].split(' or ')
    for r in details:
        bounds = r.split('-')
        valid.update(range(int(bounds[0]), 1 + int(bounds[1])))

invalid = [value for ticket in tickets for value in ticket if value not in valid]

print(sum(invalid))

good_tickets = [ticket for ticket in tickets if all(value in valid for value in ticket)]

vals = [set() for f in mine]
for t in good_tickets:
    for i, f in enumerate(t):
        vals[i].add(f)

for i, values in enumerate(vals):
    identified = False
    print(f'{i:>4}', end = ' ')
    for loc in locs:
        valid = set()
        fields = loc.split(': ')
        name = fields[0]
        details = fields[1].split(' or ')
        for r in details:
            bounds = r.split('-')
            valid.update(range(int(bounds[0]), 1 + int(bounds[1])))
        if values.difference(valid):
            print(' ', end = '')
            pass
        else:
            print('x', end = '')
            identified = True
    if not identified:
        print(f'\n\n{i} cannot be anything\n\n')
    else:
        print()

print(mine[2] * mine[5] * mine[8] * mine[10] * mine[14] * mine[18])
