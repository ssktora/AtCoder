N, K, Q = map(int, input().split())
point_list = [0 for _ in range(N)]
for _ in range(Q):
    i = int(input())
    point_list[i-1] += 1

for i in range(N):
    if K+point_list[i]-Q > 0:
        print("Yes")
    else:
        print("No")
