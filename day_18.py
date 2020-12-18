from tokenize import tokenize, NUMBER, OP 
from io import BytesIO


def read_all(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f]


def polish(s):
    g = tokenize(BytesIO(s.encode('utf-8')).readline)
    stack = []
    work = []
    for toknum, tokval, _, _, _ in g:
        if toknum == OP and tokval == '(':
            stack.append('(')
        elif toknum == OP and tokval == ')':
            prev = stack.pop()
            while prev != '(':
                work.append(prev)
                prev = stack.pop()
        elif toknum == OP and tokval in ['+', '*']:
            # if stack and stack[-1] in ['+', '*']:  # for Part 1
            if stack and stack[-1] in ['+']:
                work.append(stack.pop())
            stack.append(tokval)
        elif toknum == NUMBER:
            work.append(int(tokval))
    while stack:
        work.append(stack.pop())
    return work


def eval_polish(work):
    work.reverse()
    stack = []
    while work:
        cmd = work.pop()
        if cmd == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(a * b)
        elif cmd == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)
        else:
            stack.append(cmd)
    return stack.pop()


xs = read_all('input_18')

print(sum([eval_polish(polish(x)) for x in xs]))
