N, M = map(int, input().split())
A = list(map(int, input().split()))
X = [list(map(int, input().split())) for _ in range(N)]
# 行と列を入れ替える
X_list = [list(row) for row in zip(*X)]
frag = True
for i in range(M):
    a = A[i]
    count = 0
    for j in range(N):
        count += X_list[i][j]
    if a > count:
        frag = False
        print("No")
        break
if frag:
    print("Yes")