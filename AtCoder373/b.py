S = input()
P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = 0
position = {}
for i in range(len(S)):
    s = S[i]
    position[s] = i
now = position["A"]
for i in range(len(P)):
    p = P[i]
    ans += abs(now-position[p])
    now = position[p]
print(ans)
