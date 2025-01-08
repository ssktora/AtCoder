from collections import defaultdict
N, M = map(int, input().split())
S_list = []
for _ in range(N):
    s = input()
    S_list.append(s)

count = defaultdict(int)
for i in range(N):
    s = S_list[i]
    for j in range(M):
        if s[j] == "o":
            count[j] += 1
print(count)
ans = 0
for i in range(N):
    s = S_list[i]
    # 'o'が何文字目にあるかを取得してリストに格納
    positions = [i for i, char in enumerate(s) if char == 'o']
    print(positions)
    print(count)
    frag = True
    for p in positions:
        if count[p] == 0:
            frag = False
            break
    if frag:
        # リストの要素のキーを持つバリューを -1 する
        for pos in positions:
            count[pos] -= 1
        ans += 1
print(count)