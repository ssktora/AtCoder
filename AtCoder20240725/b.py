S = input()
frag = True
for i in range(len(S)):
    if i%2 == 0:
        if S[i] == "L":
            frag = False
            break
    else:
        if S[i] == "R":
            frag = False
            break
if frag:
    print("Yes")
else:
    print("No")