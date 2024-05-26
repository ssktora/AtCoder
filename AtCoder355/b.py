N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = []
for i in range(len(A)):
    C.append(("A",A[i]))
for i in range(len(B)):
    C.append(("B", B[i]))
C = sorted(C, key=lambda x: x[1])
pre = C[0][0]
#print(C)
frag = True
frag1 = False
for i in range(1, len(C)):
    #print(pre,C[i][0])
    if pre == C[i][0]:
        print("Yes")
        frag = False
        frag1 = True
        pre = C[i][0]
    elif frag1 and pre == C[i][0]:
        frag = False
        print("No")
        break
    else:
        pre = C[i][0]
if frag:
    print("No")