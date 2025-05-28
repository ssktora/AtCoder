N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
A.append(900000000000000)
res = 0
r = 0
for l in range(N):
    while A[r] < A[l]+M:
        r += 1
    res = max(res,r-l)

print(res)
