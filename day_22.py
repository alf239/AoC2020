
def round(first_won, xs, ys):
	if first_won(xs, ys):
		return xs[1:] + [xs[0], ys[0]], ys[1:]
	else:
		return xs[1:], ys[1:] + [ys[0], xs[0]]


def score(xs):
	return sum(x * (i + 1) for i, x in enumerate(reversed(xs)))


def rule_1(xs, ys):
	return xs[0] > ys[0]


def full_game_1(xs, ys):
	while xs and ys:
		xs, ys = round(rule_1, xs, ys)
	return score(xs + ys)


def key(xs, ys):
	return f'{xs} vs {ys}'


def rule_2(xs, ys):
	if xs[0] < len(xs) and ys[0] < len(ys):
		xx, _ = unscored_2(xs[1:xs[0] + 1], ys[1:ys[0] + 1])
		return bool(xx)
	return xs[0] > ys[0]


def unscored_2(xs, ys):
	# print(f'unscored_2({xs}, {ys})')
	seen = set()
	while xs and ys:
		k = key(xs, ys)
		xs, ys = round(lambda xx, yy: k in seen or rule_2(xx, yy), xs, ys)
		seen.add(k)
	return xs, ys


def full_game_2(xs, ys):
	# print(f'full_game_2({xs}, {ys})')
	xx, yy = unscored_2(xs, ys)
	return score(xx + yy)


def read_all(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f]


task = read_all('input_22')
xs = []
ys = []
fill = xs
for line in task:
	if line.startswith('Player '):
		continue
	elif not line:
		fill = ys
	else:
		fill.append(int(line))

print(xs, ys)

print(full_game_1(xs, ys))

print(full_game_2(xs, ys))
