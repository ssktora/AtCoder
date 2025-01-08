N, K, X = map(int, input().split())
A = list(map(int, input().split()))
ans = []
for i in range(len(A)):
    if i != K-1:
        ans.append(str(A[i]))
    else:
        ans.append(str(A[i]))
        ans.append(str(X))
print(" ".join(ans))