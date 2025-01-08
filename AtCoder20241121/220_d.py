MOD = 998244353

def solve_dp(N, A):
    # DP テーブルの初期化
    dp = [[0] * 10 for _ in range(N + 1)]
    
    # 初期状態: 長さ N の数列で、各要素が 1 通りの通り数を持つ
    for v in A:
        dp[N][v] += 1

    # 長さを短くしていく
    for i in range(N, 1, -1):
        new_dp = [0] * 10  # 新しい DP テーブルの初期化
        for x in range(10):
            for y in range(10):
                count = dp[i][x] * dp[i][y] % MOD
                new_dp[(x + y) % 10] += count
                new_dp[(x + y) % 10] %= MOD
                new_dp[(x * y) % 10] += count
                new_dp[(x * y) % 10] %= MOD
        dp[i-1] = new_dp

    # 答えを計算
    result = [dp[1][k] for k in range(10)]
    return result

# 入力を受け取る
N = int(input())
A = list(map(int, input().split()))  # 数列 A
result = solve_dp(N, A)

# 結果を出力
for k in range(10):
    print(result[k])
