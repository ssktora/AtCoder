N, X, Y = map(int, input().split())
dp = [[0, 0] for _ in range(N)]
dp[0][0] = 1
for i in range(N-1):
    dp[i][1] += X*dp[i][0]
    dp[i+1][0] += dp[i][0]

    dp[i+1][1] += Y*dp[i][1]
    dp[i+1][0] += dp[i][1]

print(dp[-1][1])