from collections import defaultdict
import sys
sys.setrecursionlimit(200005)

def dfs(v, p=-1):
    for u in to[v]:
        if u == p:
            continue
        ans[u] += ans[v]
        dfs(u,v)

n, q = map(int, input().split())
to = defaultdict(list)

for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    to[a].append(b)
    to[b].append(a)

ans = [0]*n
for _ in range(q):
    p,x = map(int, input().split())
    p -= 1
    ans[p] += x

dfs(0)
for i in range(n):
    print(ans[i])