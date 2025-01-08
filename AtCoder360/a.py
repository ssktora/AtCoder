S = list(input())
for i in range(len(S)):
    if S[i] == "M":
        m = i
    if S[i] == "R":
        r = i
if r > m:
    print("No")
else:
    print("Yes")