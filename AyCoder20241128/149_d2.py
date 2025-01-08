# 入力の読み込み
N, K = map(int, input().split())  # N: 回数, K: 制約の間隔
R, S, P = map(int, input().split())  # 各手で勝った場合のスコア
T = input().strip()  # 筐体の出す手

# グループを K 個作成
grp = ["" for _ in range(K)]
for i in range(N):
    grp[i % K] += T[i]

ans = 0

# 各グループについて計算
for k in range(K):
    r, s, p = 0, 0, 0

    # 最初の手に応じた初期スコア
    if grp[k][0] == 'r':
        p = P
    elif grp[k][0] == 's':
        r = R
    elif grp[k][0] == 'p':
        s = S

    n = len(grp[k])
    for i in range(1, n):
        # 前の手のスコアから次の手のスコアを計算
        rr = max(s, p)
        ss = max(r, p)
        pp = max(r, s)

        if grp[k][i] == 'r':
            pp += P
        elif grp[k][i] == 's':
            rr += R
        elif grp[k][i] == 'p':
            ss += S

        # スコアの更新
        r, s, p = rr, ss, pp

    ans += max(r, s, p)

print(ans)