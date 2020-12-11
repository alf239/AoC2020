x = """76
51
117
97
7
77
63
18
137
10
23
14
130
131
8
91
17
29
2
36
110
35
113
30
112
61
83
122
28
75
124
82
101
135
42
44
128
32
55
85
119
114
72
111
107
123
54
3
98
96
11
62
22
49
37
1
104
43
24
31
129
69
4
21
48
39
9
38
58
125
81
89
65
90
118
64
25
138
16
78
92
102
88
95
132
47
50
15
68
84
136
103""".split('\n')

y = [int(n) for n in x]

y.sort()

def diffs(xs):
	for a, b in zip(xs, xs[1:]):
	    yield b - a

print((1 + len([d for d in diffs(y) if d == 1])) * (1 + len([d for d in diffs(y) if d == 3])))

target = max(y) + 3
dp = [0 for i in range(target + 1)]
dp[0] = 1

for k in y:
    print(k)
    t = dp[k - 1]
    if k >= 2:
        t = t + dp[k - 2]
    if k >= 3:
        t = t + dp[k - 3]
    dp[k] = t


print(dp[target - 3])



