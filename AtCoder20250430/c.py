N = int(input())
A = list(map(int, input().split()))
p = 0
p_list = []
for i in range(N):
    p += A[i]
    p_list.append(p)

min_p = min(p_list)
if min_p < 0:
    print(p_list[-1]+(-min_p))
else:
    print(p_list[-1])