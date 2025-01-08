from itertools import product

def count_valid_key_combinations(N, K, tests):
    # 全ての鍵の正しい・ダミーの組み合わせを生成
    all_combinations = list(product([0, 1], repeat=N))
    #print(all_combinations)
    valid_combinations_count = 0
    
    # 各鍵の組み合わせについて
    for combination in all_combinations:
        is_valid = True
        
        for (C, keys, result) in tests:
            correct_key_count = sum(combination[key - 1] for key in keys)
            
            if (result == 'o' and correct_key_count < K) or (result == 'x' and correct_key_count >= K):
                is_valid = False
                break
        
        if is_valid:
            valid_combinations_count += 1
    
    return valid_combinations_count
N, M, K = map(int, input().split())
test = []
for i in range(M):
    a_list = list(map(str, input().split()))
    c = a_list.pop(0)
    c = int(c)
    r = a_list.pop(-1)
    b_list = [int(element) for element in a_list]
    test.append((c,b_list,r))

print(count_valid_key_combinations(N, K, test))

