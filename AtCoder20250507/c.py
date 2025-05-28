H,W = map(int, input().split())
S = [input() for _ in range(H)]
cookie = []
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            cookie.append((i,j))

print(cookie)

from collections import defaultdict
i_count = defaultdict(int)
j_count = defaultdict(int)
for i in range(len(cookie)):
    p = cookie[i]
    i_count[p[0]] += 1
    j_count[p[1]] += 1

value_count_i = defaultdict(int)
for k, v in i_count.items():
    value_count_i[v] += 1

value_count_j = defaultdict(int)
for k, v in j_count.items():
    value_count_j[v] += 1

for k, v in value_count_i.items():
    if v == 1:
        ans_i = k+1
        break

 for k, v in value_count_j.items():
    if v == 1:
        ans_j = k+1
        break   

print(ans_i,ans_j)
