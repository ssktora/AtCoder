N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
if min(A) > min(B):
    print(-1)
else:
    check = True
    for i in range(N-1):
        if B[i] < A[i]:
            print(A[i])
            check = False
            break