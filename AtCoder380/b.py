S = input()
start = True
count = 0
ans = []
for s in S[1:]:
    if s == "-":
        count += 1
    elif s == "|":
        ans.append(str(count))
        count = 0

print(" ".join(ans))