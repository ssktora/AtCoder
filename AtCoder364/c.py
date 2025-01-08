N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A,reverse=True)
B = sorted(B,reverse=True)
ans_a = 0
ans_b = 0
pa = 0
pb = 0
frag = True
for i in range(len(A)):
    a = A[i]
    pa += a
    b = B[i]
    pb += b
    if pa > X:
        ans_a = i+1
        frag = False
        break
    if pb > Y:
        ans_b = i+1
        frag = False
        break

if frag:
    print(N)
