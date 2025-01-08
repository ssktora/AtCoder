S = input()
T = input()
frag = True
if len(S) == len(T):
    for i in range(len(S)):
        if S[i] != T[i]:
            print(i+1)
            frag = False
            break
    if frag:
       print(0)
elif len(S) > len(T):
    for i in range(len(T)):
        if S[i] != T[i]:
            print(i+1)
            frag = False
            break
    if frag:
       print(len(T)+1)
else:
    for i in range(len(S)):
        if S[i] != T[i]:
            print(i+1)
            frag = False
            break
    if frag:
       print(len(S)+1)