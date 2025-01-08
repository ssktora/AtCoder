N, M = map(int, input().split())
H = list(map(int, input().split()))
ans = 0
p = M
frag = True
for i in range(N):
    if p < H[i]:
        print(ans)
        frag = False
        break
    else:
        p -= H[i]
        ans += 1
if frag:
    print(ans)