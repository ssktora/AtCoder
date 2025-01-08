from itertools import product

def solve(R):
    # Rの要素それぞれが桁数の制約を持つ
    ranges = [map(str, range(1, r + 1)) for r in R]
    
    result = []
    for combination in product(*ranges):
        str_list = list(combination)
        int_list = [int(x) for x in str_list]
        result.append(int_list)
    
    return result

# 入力例
N, K = map(int, input().split())
R = list(map(int, input().split()))

result = solve(R)
ans_list = []
for r_list in result:
    if sum(r_list)%K==0:
        a_list = [str(x) for x in r_list]
        ans_list.append(a_list)

for ans in ans_list:
    print(" ".join(ans))