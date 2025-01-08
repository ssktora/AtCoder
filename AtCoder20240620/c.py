N = int(input())
H = list(map(int, input().split()))
max_n = 0
frag = True
for h in H:
    if max_n < h:
        max_n = h
    if max_n-h >= 2:
        print("No")
        frag = False
        break
if frag:
    print("Yes")