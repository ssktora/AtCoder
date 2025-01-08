N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = set(map(int, input().split()))  # 集合に変換して高速な存在判定を行う
X = int(input())

stage = [False] * (X + 1)
stage[0] = True

for i in range(X):
    if stage[i]:
        for a in A:
            next_pos = i + a
            if next_pos <= X and next_pos not in B:  # Bの中にないかを集合で確認
                stage[next_pos] = True

print("Yes" if stage[X] else "No")


