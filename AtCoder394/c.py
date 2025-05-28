S = input()
ans = []
frag = False
count = 0
for s in S:
    if frag:
        if s == "W":
            count += 1
        elif s == "A":
            frag = False
            ans.append("A")
            ans.append("C"*count)
            count = 0
        else:
            frag = False
            ans.append("W"*count)
            ans.append(s)
            count = 0
    else:
        if s == "W":
            frag = True
            count += 1
        else:
            ans.append(s)
if frag and S[-1] == "W":
    ans.append("W"*count)

print("".join(ans))