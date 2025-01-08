K, X = map(int, input().split())
ans = []
for i in range(X-K,X+K):
    ans.append(str(i))
print(" ".join(ans))