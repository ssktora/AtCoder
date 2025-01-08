N, T, P = map(int, input().split())
L = list(map(int, input().split()))

for i in range(1,101):
    check = [x + i for x in L]
    p = 0
    for c in check:
        if c >= T:
            p += 1
    if P <= p:
        print(i)
        break