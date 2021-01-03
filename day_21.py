
def read_all(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f]


def parse_line(s):
    ingridients, allergens = s.split(' (contains ')
    return set(ingridients.split(' ')), set(allergens[:-1].split(', '))


def multimap_add(mm, k, v):
    vals = mm.get(k, [])
    vals.append(v)
    mm[k] = vals


xs = read_all('input_21')


recipes = []
advice = {}

for x in xs:
    ings, alls = parse_line(x)
    for a in alls:
        multimap_add(advice, a, ings)
    recipes.append(ings)

allergens = {}
for a, sets in advice.items():
    allergens[a] = set.intersection(*sets)

danger = set(food for _, foods in allergens.items() for food in foods)

print('Task 1', len([1 for ings in recipes for i in ings if i not in danger]))

# Canonical list:
#
# 'dairy':     'fntg'
# 'eggs':      'gtqfrp'
# 'fish':      'xlvrggj'
# 'peanuts':   'rlsr'
# 'sesame':    'xpbxbv'
# 'shellfish': 'jtjtrd'
# 'soy':       'fvjkp'
# 'wheat':     'zhszc'
#
# Task 2: fntg,gtqfrp,xlvrggj,rlsr,xpbxbv,jtjtrd,fvjkp,zhszc
