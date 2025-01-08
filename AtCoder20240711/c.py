N = int(input())
H = list(map(int, input().split()))
ans = 0
p = 0
for i in range(1,N):
    if H[i-1] >= H[i]:
        p += 1
    else:
        ans = max(ans,p)
        p = 0
ans = max(ans,p)
print(ans)
