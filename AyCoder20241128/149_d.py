N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()
dp = [0 for _ in range(N+1)]
output = []
for i in range(N):
    t = T[i]
    if i < K:
        if t == "r":
            dp[i+1] = dp[i] + P
            output.append("p")
        elif t == "s":
            dp[i+1] = dp[i] + R
            output.append("r")
        else:
            dp[i+1] = dp[i] + S
            output.append("s")
    else:
        if t == "r":
            if output[i-K] != "p":
                dp[i+1] = dp[i] + P
                output.append("p")
            else:
                dp[i+1] = dp[i]
                output.append("r")
        elif t == "s":
            if output[i-K] != "r":
                dp[i+1] = dp[i] + R
                output.append("r")
            else:
                dp[i+1] = dp[i]
                output.append("s")
        else:
            if output[i-K] != "s":
                dp[i+1] = dp[i] + S
                output.append("s")
            else:
                dp[i+1] = dp[i]
                output.append("p")
print(dp[N])



