N, M = map(int, input().split())
frag = [True for _ in range(N)]
for i in range(M):
    a, b = input().split()
    a = int(a)
    if b == "F":
        print("No")
    else:
        if frag[a-1]:
            print("Yes")
            frag[a-1] = False
        else:
            print("No")
    