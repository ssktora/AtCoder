def calculate_sum(N, M):
    MOD = 998244353
    
    # N+1は最大2^60なので、60ビットを想定
    bit_length = 60
    
    # 各ビットごとの貢献を計算
    result = 0
    for i in range(bit_length):
        bit_mask = 1 << i
        print(bit_mask, M)
        # N までの数で i ビット目が 1 になる数
        if M & bit_mask:
            # Mの i ビット目が1であるとき、k の i ビット目が 1 になる数を数える
            count = ((N + 1) // (bit_mask << 1)) * bit_mask
            count += max(0, (N + 1) % (bit_mask << 1) - bit_mask)
            result += count
            result %= MOD
            
    return result

N, M = map(int, input().split())
print(calculate_sum(N, M))