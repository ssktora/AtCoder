N, M = map(int, input().split())
A = list(map(int, input().split()))
ans = []
for i in range(1,N+1):
    if i not in A:
        ans.append(str(i))
print(len(ans))
print(" ".join(ans))