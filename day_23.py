from dataclasses import dataclass
from typing import List


@dataclass
class Node:
    id: int
    next: 'Node'


def game(s, N=None):
    idx = {}
    first = None
    last = Node(-1, None)  # sentinel
    for c in input:
        node = Node(int(c), None)
        if not first:
            first = node
        idx[node.id] = node
        last.next = node
        last = last.next
    last.next = first
    return idx


def cut(node, n):
    x = node
    for _ in range(n - 1):
        x = x.next
    tail = x.next
    x.next = None
    return node, x, tail


def as_list(node):
    x = node
    res = []
    while x:
        res.append(x.id)
        x = x.next
        if x == node:
            break
    return res


def highest_lower(x, N, exclude):
    while True:
        x = (x - 1) if x > 1 else N
        if x not in exclude:
            return x


def step(state, node, pu_cnt=3):
    N = len(state)
    pu_b, pu_e, tail = cut(node.next, pu_cnt)
    node.next = tail
    dest = highest_lower(node.id, N, set(as_list(pu_b)))
    end = state[dest]
    pu_e.next = end.next
    end.next = pu_b
    return tail


def to_str(node):
    return ''.join(str(x) for x in as_list(node))


input = '186524973'
# input = '389125467'  # Task example

state = game(input)
cup = state[int(input[0])]

for i in range(100):
    cup = step(state, cup)

task1 = to_str(state[1])[1:]

print('Task 1:', task1)
assert task1 == '45983627'


state2 = game(input)
end = state2[int(input[-1])]

for i in range(len(state2), 1000000):
    node = Node(i + 1, end.next)
    state2[i + 1] = node
    end.next = node
    end = node

cup = state2[int(input[0])]
for i in range(10000000):
    cup = step(state2, cup)
    if i % 1000000 == 0:
        print(i, end='\t')
print()

ref = state2[1]
print('Task 2:', ref.next.id * ref.next.next.id)
