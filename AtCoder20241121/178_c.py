N = int(input())
p = 10**9+7
dp = [[0,0,0,0] for _ in range(N+1)]
dp[0][0] = 1
for i in range(1,N+1):
    dp[i][0] = (dp[i-1][0] * 8)%p
    dp[i][1] = (dp[i-1][1] * 9 + dp[i-1][0])%p
    dp[i][2] = (dp[i-1][2] * 9 + dp[i-1][0])%p
    dp[i][3] = (dp[i-1][3] * 10 + dp[i-1][1] + dp[i-1][2])%p

print(dp[N][3])
