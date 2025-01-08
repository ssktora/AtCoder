N = int(input())
frag = True
s_list = ["s"]
for i in range(N):
    S = input()
    if S == "sweet":
        if s_list[-1] == "sweet" and i != N-1:
            frag = False
            break
        else:
            s_list.append(S)
    else:
        s_list.append(S)
if frag:
    print("Yes")
else:
    print("No")