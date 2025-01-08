
N, M = map(int, input().split())
S_list = []
for _ in range(N):
    s = input()
    S_list.append(s)

import itertools

# 部分集合をすべて列挙
subsets = []
for r in range(len(S_list) + 1):
    subsets.extend(itertools.combinations(S_list, r))

from collections import defaultdict
ans = 1000000
for subset in subsets:
    count = defaultdict(int)
    for i in range(len(subset)):
        s = subset[i]
        for j in range(M):
            if s[j] == "o":
                count[j] += 1
    if len(count) == M:
        p = len(subset)
        ans = min(ans,p)
print(ans)
    
