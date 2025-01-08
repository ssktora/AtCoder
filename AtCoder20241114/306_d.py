N = int(input())
dp = [[-float("inf"), -float("inf")] for _ in range(N + 1)]
dp[0][0] = 0  # 初期状態：生きていてお腹を壊していない

for i in range(1, N + 1):
    x, y = map(int, input().split())

    # お腹を壊していない状態からの遷移
    if dp[i - 1][0] != -float("inf"):
        # 解毒剤入り料理
        if x == 0:
            dp[i][0] = max(dp[i][0], dp[i - 1][0] + y)  # お腹を壊していない状態のまま
        # 毒入り料理
        else:
            dp[i][1] = max(dp[i][1], dp[i - 1][0] + y)  # お腹を壊す

    # お腹を壊している状態からの遷移
    if dp[i - 1][1] != -float("inf"):
        # 解毒剤入り料理
        if x == 0:
            dp[i][0] = max(dp[i][0], dp[i - 1][1] + y)  # お腹を壊していない状態に戻る

    # i番目の料理を食べない場合も、最大値をそのまま保持する
    dp[i][0] = max(dp[i][0], dp[i - 1][0])
    dp[i][1] = max(dp[i][1], dp[i - 1][1])


print(max(dp[-1]))