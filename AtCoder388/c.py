from bisect import bisect_left
N = int(input())
A = list(map(int, input().split()))
ans = 0
L = 1
for i in range(N):
    a = A[i]
    j = bisect_left(A, a*2)
    # for j in range(L,N):
    #     if a*2 <= A[j]:
    ans += N-j
    L = j
print(ans)

