def get_add(T, h):
    # Tに対する処理
    mod_t = T % 3
    p = 0
    
    if h >= 5:
        if mod_t == 1:
            p += 2
            h -= 4
        elif mod_t == 2:
            p += 1
            h -= 3
        p += 3 * (h // 5)
    
    # 残りのhに対する処理
    q = h % 5
    if q == 4:
        p += 3
    else:
        p += q
    
    return p

N = int(input())
H = list(map(int, input().split()))
T = 0
for i in range(N):
    t = get_add(T, H[i])
    T += t

print(T)