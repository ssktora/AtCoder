N, K = map(int, input().split())
A = list(map(int, input().split()))

A = sorted(A)
ans = float('inf')

for i in range(K + 1):
    p = A[N - K + i - 1] - A[i]
    ans = min(ans, p)

print(ans)
