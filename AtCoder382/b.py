N, D = map(int, input().split())
S = list(input())
p = 0
for i in range(N-1,-1,-1):
    if S[i] == "@":
        S[i] = "."
        p += 1
    if p == D:
        break
print("".join(S))
