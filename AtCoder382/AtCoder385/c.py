def check(h_list):
    

N = int(input())
H = list(map(int, input().split()))
from collections import defaultdict
h_dic = defaultdict(list)
for i in range(N):
    h_dic[H[i]].append(i)

ans = 0
for key, h_list in h_dic.items():
    p = check(h_list)
    ans = max(ans,p)

print(ans)
