N = int(input())
K = list(map(int, input().split()))
import itertools

# 0と1の順列を列挙
all_permutations = list(itertools.product([0, 1], repeat=N))

ans = 99999999999999999999999
for perm in all_permutations:
    perm = list(perm)
    a_list = []
    b_list = []
    for i in range(len(perm)):
        if perm[i] == 0:
            a_list.append(K[i])
        else:
            b_list.append(K[i])
    if sum(a_list) >= sum(b_list):
        ans = min(ans,sum(a_list))
    else:
        ans = min(ans, sum(b_list))


print(ans)