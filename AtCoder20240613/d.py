S = input()
MOD = 10**9+7
n = len(S)

dp = [[0] * 13 for _ in range(n+1)]
dp[0][0] = 1
for i in range(n):
    for r in range(13):
        if dp[i][r] == 0:
            continue

        if S[i] == "?":
            for digit in range(10):
                new_r = (r*10+digit)%13
                dp[i+1][new_r] = (dp[i+1][new_r] + dp[i][r]) % MOD
        else:
            digit = int(S[i])
            new_r = (r*10+digit)%13
            dp[i+1][new_r] = (dp[i+1][new_r] + dp[i][r]) % MOD
print(dp[n][5])