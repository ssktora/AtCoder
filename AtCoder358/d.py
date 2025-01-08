N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A = sorted(A)
ans = 0
import bisect
frag = True
for i in range(M):
    b = B[i]
    # b より大きい最初の要素のインデックスを探す
    index = bisect.bisect_left(A, b)

    # b を超える要素がリストに存在する場合
    if index < len(A):
        min_value = A[index]
        # 最小の値をリスト A から削除する
        A.pop(index)
        print(min_value)
        ans += min_value
    else:
        frag = False
        print(-1)
        break
if frag:
    print(ans)