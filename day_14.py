
def read_all(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f]

mem = {}

for x in read_all('input_14'):
    if x.startswith('mask = '):
        mask = x[7:]
        and_mask = int(mask.replace('X', '1'), 2)
        or_mask = int(mask.replace('X', '0'), 2)
    elif x.startswith('mem['):
        fields = x.split(' = ')
        address = int(fields[0][4:-1])
        value = int(fields[1])
        mem[address] = (value & and_mask) | or_mask

print(sum(mem.values()))
