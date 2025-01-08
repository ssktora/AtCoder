def shortest_path_with_obstacles(n, current_pos, target_pos, blocked_position):
     # インデックスを1ベースから0ベースに変換
    def convert_to_index(position):
        return (position - 1) % n
        
    # 時計回りの移動距離を計算する関数
    def calculate_clockwise_distance(current, target):
        distance = 0
        while current != target:
            current = (current + 1) % n  # 時計回りに1マス進む
            distance += 1
            if current == blocked_position:
                return float('inf')  # 通れないマスがあった場合、大きな値を返す
        return distance

    # 反時計回りの移動距離を計算する関数
    def calculate_counter_clockwise_distance(current, target):
        distance = 0
        while current != target:
            current = (current - 1) % n  # 反時計回りに1マス戻る
            distance += 1
            if current == blocked_position:
                return float('inf')  # 通れないマスがあった場合、大きな値を返す
        return distance
        
    # 現在位置と目的地をインデックスに変換
    current_pos = convert_to_index(current_pos)
    target_pos = convert_to_index(target_pos)
    blocked_position = convert_to_index(blocked_position)
    

    # 各方向の距離を計算
    clockwise_distance = calculate_clockwise_distance(current_pos, target_pos)
    counter_clockwise_distance = calculate_counter_clockwise_distance(current_pos, target_pos)

    # どちらの距離が短いかを判定
    if clockwise_distance < counter_clockwise_distance:
        distance = clockwise_distance
    elif counter_clockwise_distance < clockwise_distance:
        distance = counter_clockwise_distance
    else:
        distance = clockwise_distance

    return distance

N, Q = map(int, input().split())
L = 1
R = 2
ans = 0
for i in range(Q):
    H, T = map(str, input().split())
    T = int(T)
    if H == "R":
        distance = shortest_path_with_obstacles(N, R, T, L)
        ans += distance
        R = T
    else:
        distance = shortest_path_with_obstacles(N, L, T, R)
        ans += distance
        L = T
    #print(ans)

print(ans)
