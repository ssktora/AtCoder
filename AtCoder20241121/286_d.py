N, X = map(int, input().split())
a = []
for i in range(N):
    A, B = map(int, input().split())
    for j in range(B):
        a.append(A)
def subset_sum(a,X):
    n = len(a)
    dp = [[False] * (X+1) for _ in range(n+1)]
    dp[0][0] = True

    for i in range(1,n+1):
        for j in range(X+1):
            dp[i][j] = dp[i-1][j]
            if j >= a[i-1]:
                dp[i][j] = dp[i][j] or dp[i-1][j-a[i-1]]
    return dp[n][X]

if subset_sum(a,X):
    print("Yes")
else:
    print("No")