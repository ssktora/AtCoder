N = int(input())
A = list(map(int, input().split()))
x2 = 0
for i in range(N):
    if i%2==0:
        x2 += A[i]
    else:
        x2 -= A[i]

x = x2/2
ans = [0 for _ in range(N)]
ans[0] = x
for i in range(N-1):
    ans[i+1] = A[i] - ans[i]
for i in range(N):
    ans[i] *= 2
    ans[i] = str(int(ans[i]))
print(" ".join(ans))
