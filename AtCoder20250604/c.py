S = list(input())
T = list(input())
from collections import defaultdict
counter_s = defaultdict(int)
counter_t = defaultdict(int)
for c in S:
    counter_s[c] += 1
for c in T:
    counter_t[c] += 1


for p in "atcoder":
    M = max(counter_s[p], counter_t[p])
    if counter_s["@"] < M - counter_s[p] or counter_t["@"] < M - counter_t[p]:
        print("No")
        exit()
    counter_s["@"] -= M - counter_s[p]
    counter_s[p] = M
    counter_t["@"] -= M - counter_t[p]
    counter_t[p] = M

if counter_s == counter_t:
    print("Yes")
else:
    print("No")