N, M = map(int, input().split())
A = list(map(int, input().split()))
new_A = []
for a in A:
    new_A.append(-a)
# heapq
import heapq

heapq.heapify(new_A) # 優先度付きキューの作成

for i in range(M):
    a = heapq.heappop(new_A)
    a = -a
    a = a//2
    heapq.heappush(new_A, -a)

print(-sum(new_A))