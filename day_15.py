x = [14,8,16,0,1,17]

N = 30000000

dp = [-1] * (N + 1)

for i in range(N):
    if i < len(x):
        dp[x[i]] = i
        last = x[i]
    else:
        said = dp[last]
        dp[last] = i - 1
        if said == -1:
            last = 0
        else:
            last = i - 1 - said
print(last)

