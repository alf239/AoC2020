
def read_all(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f]

def write_with_mask(mem, and_mask, or_mask, mask, addr, val):
    # print(f'write_with_mask(mem, {and_mask}, {or_mask}, {mask}, {addr}, {val})')
    if mask == '':
        final_addr = int(addr) & and_mask | or_mask
        # print(f'mem[{final_addr}] = {val}')
        mem[final_addr] = val
    else:
        x = mask[0]
        if x == '0':
            and_mask = (and_mask << 1) + 1
            or_mask = or_mask << 1
            write_with_mask(mem, and_mask, or_mask, mask[1:], addr, val)
        elif x == '1':
            and_mask = and_mask << 1
            or_mask = (or_mask << 1) + 1
            write_with_mask(mem, and_mask, or_mask, mask[1:], addr, val)
        else:
            and_mask = and_mask << 1
            write_with_mask(mem, and_mask, or_mask << 1, mask[1:], addr, val)
            write_with_mask(mem, and_mask, (or_mask << 1) + 1, mask[1:], addr, val)

mem = {}

for x in read_all('input_14'):
    if x.startswith('mask = '):
        mask = x[7:]
    elif x.startswith('mem['):
        fields = x.split(' = ')
        address = int(fields[0][4:-1])
        value = int(fields[1])
        write_with_mask(mem, 0, 0, mask, address, value)

# print(mem)
print(sum(mem.values()))
