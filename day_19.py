import regex as re

def read_all(filename):
    with open(filename) as f:
        return [line.strip() for line in f]
 
cmds = read_all('input_19')

rules = []
lines = []
fill = rules
# print(cmds)
for cmd in cmds:
    if cmd == '':
        fill = lines
    else:
        fill.append(cmd)

def parse_rule(r):
    rs = r.split(': ')
    return (rs[0], rs[1])

rules = dict(parse_rule(r) for r in rules)
# 8: 42 | 42 8
# 11: 42 31 | 42 11 31
rules['8'] = '42 | 42 8'
rules['11'] = '42 31 | 42 11 31'

def regexp_for(rule, rules):
    global capture
    # print(f'regexp_for({rule}, rules)')
    if rule == '42 | 42 8':  # 8: 42 | 42 8
        return regexp_for(rules['42'], rules) + '+'
    elif rule == '42 31 | 42 11 31':  # 11: 42 31 | 42 11 31
        a = regexp_for(rules['42'], rules)
        b = regexp_for(rules['31'], rules)
        return '(?:' + '|'.join(['(?:' + a * i + b * i + ')' for i in range(1, 20)]) + ')'
    elif rule.startswith('"'):
        return rule[1:-1]
    elif '|' in rule:
        disjuncts = rule.split(" | ")
        return '(?:' + '|'.join(regexp_for(r, rules) for r in disjuncts) + ')'
    elif not rule:
        raise "ooops"
    else:
        terms = rule.split(' ')
        return ''.join(regexp_for(rules[r], rules) for r in terms)

rx = regexp_for(rules['0'], rules) + '$'
regexp = re.compile(rx)

print(rx)
 
print(len([l for l in lines if regexp.match(l)]))



