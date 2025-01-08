N = int(input())
B = list(map(int, input().split()))

A = [B[0]]
for i in range(len(B)):
    A.append(B[i])
    if A[-2] <= B[i] and A[-1] <= B[i]:
        continue
    else:
        A[-2] = B[i]
    #print(A)

print(sum(A))