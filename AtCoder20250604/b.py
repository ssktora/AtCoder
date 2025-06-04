N = int(input())
A = list(map(int, input().split()))
ans = []
for i in range(N-1):
    ans.append(A[i])
    if A[i] < A[i+1] and A[i]+1 != A[i+1]:
        p = A[i] + 1
        while p != A[i+1]:
            ans.append(p)
            p += 1
    elif A[i] > A[i+1] and A[i]-1 != A[i+1]:
        p = A[i] - 1
        while p != A[i+1]:
            ans.append(p)
            p -= 1
ans.append(A[-1])
print(*ans)