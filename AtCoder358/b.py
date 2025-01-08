N, A = map(int, input().split())
T = list(map(int, input().split()))
ans = 0
wait = 0
for i in range(N):
    if T[i] >= ans:
        ans += T[i] - ans
        ans += A
        print(ans)
    else:
        ans += A
        print(ans)
