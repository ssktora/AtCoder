N, C = map(int,input().split())
T = list(map(int,input().split()))
ans = 1
now = T[0]
for i in range(1,N):
    if T[i] - now >= C:
        ans += 1
        now = T[i]
print(ans)
