N, M = map(int, input().split())
AB_list = []
for i in range(N):
    A,B = map(int, input().split())
    AB_list.append((A,B))

ans = 0
day = 0
AB_list = sorted(AB_list, key=lambda x: x[1], reverse=True)
while True:
    if len(AB_list) != 0:
        ans += AB_list[0][1]
        day += 1
        new_list = []
        for v in AB_list:
            if v[0]+day <= M:
                new_list.append(v)
        AB_list = sorted(new_list, key=lambda x: x[1], reverse=True)

    else:
        break

print(ans)