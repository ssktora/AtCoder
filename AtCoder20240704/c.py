N = int(input())
V = list(map(int, input().split()))

# リストを降順にソート
V.sort()

# 初期値は最大の要素
k = V[0]

# 残りの要素を使って計算
for i in range(1, N):
    k = (k + V[i]) / 2

print(k)