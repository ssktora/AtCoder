N, M  = map(int, input().split())
from collections import defaultdict
cook = defaultdict(list)
not_lile = defaultdict(int)
for i in range(M):
    a_list = list(map(int, input().split()))
    k = a_list.pop(0)
    not_like[i] = k
    cook[i] = a_list

b_list = list(map(int, input().split()))

for i in range(N):