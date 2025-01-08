N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int,input().split()))

dp1 = [True]
dp2 = [True]
for i in range(1,N):
    if dp1[i-1] == True and abs(A[i-1]-A[i])<=K:
        dp1.append(True)

    elif dp2[i-1] == True and abs(B[i-1]-A[i])<=K:
        dp1.append(True)

    else:
        dp1.append(False)

    if dp1[i-1] == True and abs(A[i-1]-B[i])<=K:
        dp2.append(True)

    elif dp2[i-1] == True and abs(B[i-1]-B[i])<=K:
        dp2.append(True)

    else:
        dp2.append(False)
        
    # print(dp1)
    # print(dp2)

if dp1[-1] or dp2[-1]:
    print("Yes")
else:
    print("No")