N = int(input())
a = list(map(int, input().split()))
def find_good_ball_placement(N, a):
    balls = [0] * N

    # ボールの配置を決める
    for i in range(N - 1, -1, -1):
        sum_multiples = sum([balls[j] for j in range(i, N, i + 1)])
        if sum_multiples % 2 != a[i]:
            balls[i] = 1
    
    return balls

# 関数の呼び出し
result = find_good_ball_placement(N, a)
ans = []
for i in range(len(result)):
    if result[i] == 1:
        ans.append(str(i+1))
print(len(ans))
print(" ".join(ans))
