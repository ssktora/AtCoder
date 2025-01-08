N, K = map(int, input().split())
A = list(map(str, input().split()))
ans = []
for i in range(K,0,-1):
    ans.append(A[-i])

for i in range(N-K):
    ans.append(A[i])

print(" ".join(ans))