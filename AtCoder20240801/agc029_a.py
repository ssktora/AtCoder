S = input()
ans = []
for i in range(len(S)):
    if S[i] == "W":
        ans.append(i-len(ans))

print(sum(ans))