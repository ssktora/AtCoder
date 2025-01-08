N, D = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(N)]
import itertools
original_list = [i for i in range(N)]
# 2つの要素の組み合わせを生成
pairs = list(itertools.combinations(original_list, 2))
# p_ansが整数かどうかを判定する関数
def is_integer(num):
    # 浮動小数点数として値を比較し、整数であればTrueを返す
    return num.is_integer()

ans = 0
for pair in pairs:
    i = pair[0]
    j = pair[1]
    Y = S[i]
    Z = S[j]
    p = 0
    for d in range(len(Y)):
        p += (Y[d]-Z[d])**2
    p_ans = p**(1/2)
    # p_ansが整数であるかどうかを判定する
    if is_integer(p_ans):
        ans += 1

print(ans)