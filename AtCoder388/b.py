N, D = map(int, input().split())
t_list = []
l_list = []
for i in range(N):
    t, l = map(int, input().split())
    t_list.append(t)
    l_list.append(l)
for k in range(1,D+1):
    ans = -1
    for i in range(N):
        p = t_list[i]*(l_list[i]+k)
        ans = max(ans,p)
    print(ans)