N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
p_list = []
for i in range(1,N+1):
    p_list.append((("a",i),A[i-1]))
for i in range(M):
    p_list.append((("b",i),B[i]))
p_list.sort(key=lambda x: x[1])
print(p_list)
big = 100000000000000000000000
ans = big
ans_dic = {}
for i in range(len(p_list)):
    p = p_list[i]
    if p[0][0] == "b":
        ans_dic[p[0][1]] = ans
    else:
        ans = min(ans,p[0][1])
ans_dic = sorted(ans_dic.items())
for i in range(len(ans_dic)):
    if ans_dic[i][1] != big:
        print(ans_dic[i][1])
    else:
        print(-1)