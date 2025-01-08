N = int(input())
X = list(map(int, input().split()))
P = list(map(int, input().split()))
Q = int(input())
a_dic = {}
count = 0
for i in range(X[0], X[-1]+1):
    if i in X:
        s = X.index(i)
        count += P[s]
        a_dic[i] = count
    else:
        a_dic[i] = count
#print(a_dic)

for i in range(Q):
    l, r = map(int, input().split())
    if X[0] <= l <= r <= X[-1]: 
        ans = a_dic[r]-a_dic[l]
    elif l <= r <= X[0] <= X[-1]:
        ans = 0
    elif l <= X[0] <= r <= X[-1]:
        ans = a_dic[r]
    elif X[0] <= l <= X[-1] <= r:
        ans = a_dic[X[-1]] - a_dic[l]
    else:
        ans = 0
    print(ans)
