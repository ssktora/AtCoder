N, T = map(int, input().split())
S = input()
X = list(map(int, input().split()))
ans = (N*(N-1))/2
a_list = []
for i in range(len(S)):
    if S[i] == "1":
        a = (S[i],X[i],X[i]+T)
    else:
        a = (S[i],X[i],X[i]-T)
    a_list.append(a)

before_count = {}
after_count = {}
# '0' の数を数える
num_zeros = S.count('0')
for i in range(len(a_list)):
    if a_list[i][0] == "1":
        before_count[a_list[i]] = num_zeros
    else:
        num_zeros -= 1

# 3つ目の要素で昇順に並べ替え
a_list = sorted(a_list, key=lambda x: (x[2], -x[1]))
num_zeros = S.count('0')
for i in range(len(a_list)):
    if a_list[i][0] == "1":
        after_count[a_list[i]] = num_zeros
    else:
        num_zeros -= 1

ans = 0
for k in before_count.keys():
    ans += before_count[k]-after_count[k]
print(ans)
