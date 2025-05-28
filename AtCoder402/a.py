S = input()
ans = ""
for i in range(len(S)):
    if S[i].islower():
        ans += S[i]
print(ans)