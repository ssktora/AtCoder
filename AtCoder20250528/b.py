N, A, B = map(int, input().split())

# チェッカーパターンの基本タイルを作成
tiles = []
for i in range(N):
    row = []
    for j in range(N):
        if (i + j) % 2 == 0:
            row.append('.')
        else:
            row.append('#')
    tiles.append(row)

X = []
for i in range(N):
    for a in range(A):
        row = ""
        for j in range(N):
            row += tiles[i][j] * B
        X.append(row)

for row in X:
    print(row)