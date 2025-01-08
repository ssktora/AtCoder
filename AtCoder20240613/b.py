N = int(input())
P = list(map(int, input().split()))
Q = [i for i in range(1,N+1)]
ans = 0
for i in range(N):
    if P[i] != Q[i]:
        ans += 1

if ans == 2 or ans == 0:
    print("YES")
else:
    print("NO")