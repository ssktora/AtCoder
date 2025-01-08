L, R = map(int, input().split())
def min_modulo(L, R):
    min_mod = float('inf')
    for i in range(L, R):
        for j in range(i + 1, R + 1):
            mod = (i % 2019) * (j % 2019) % 2019
            if mod < min_mod:
                min_mod = mod
                if min_mod == 0:  # 既知の最小値が0の場合、これ以上の最適化は不要
                    return 0
    return min_mod


result = min_modulo(L, R)
print(result)