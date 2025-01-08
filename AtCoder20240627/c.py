N = int(input())
s_list = []
for i in range(N):
    s = list(input())
    s_list.append(s)
    
s_list = [tuple(sorted(s)) for s in s_list]

# 要素をカウントするための辞書を作成
from collections import Counter
element_counts = Counter(s_list)

# カウント数に基づいて降順にソート
sorted_elements = sorted(element_counts.items(), key=lambda x: x[1], reverse=True)

import math
ans = 0
#print(sorted_elements)
for i in range(len(sorted_elements)):
  n = sorted_elements[i][1]
  p = n*(n-1)/2
  ans += p
print(int(ans))

    
