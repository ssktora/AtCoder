S = input()
mod = 10**9 + 7
n = len(S)
dp = [[0] * (n + 1) for _ in range(9)]

# Initialize the base case
for j in range(n + 1):
    dp[0][j] = 1  # dp[0][j] is 1 for all j because an empty subsequence is counted once

# Iterate over each character in "chokudai"
for i in range(1, 9):
    for j in range(1, n + 1):
        dp[i][j] = dp[i][j - 1]  # Carry over the count from the left
        if S[j - 1] == "chokudai"[i - 1]:
            dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % mod  # Add matching count

print(dp[8][n])