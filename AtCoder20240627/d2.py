N, M = map(int, input().split())
import heapq
jobs = [[] for _ in range(M)]
for i in range(N):
    A,B = map(int, input().split())
    if A <= M:
        jobs[M-A].append(B)
ans = 0
q = []
for i in range(M-1,-1,-1):
    for b in jobs[i]:
        heapq.heappush(q, -b)
    if q:
        ans += -heapq.heappop(q)

print(ans)