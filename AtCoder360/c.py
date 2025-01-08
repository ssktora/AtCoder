N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))
ans = sum(W)
from collections import defaultdict
a_dic = defaultdict(list)
for i in range(N):
    a_dic[A[i]].append(W[i])
for v in a_dic.values():
    ans -= max(v)
print(ans)