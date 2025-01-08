N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = [0 for _ in range(N+1)]
for i in range(N):
    # print(A)
    # print(B)
    # print(ans)
    # print("-----")
    b = B[i]
    if A[i] < b:
        ans[i] += A[i]
        b -= A[i]
        A[i] = 0
        if A[i+1] < b:
          ans[i+1] += A[i+1]
          b -= A[i+1]
          A[i+1] = 0
        else:
          A[i+1] -= b
          ans[i+1] += b
    else:
        ans[i] += b
        A[i] -= b
# print(A)
# print(B)
# print(ans)
print(sum(ans))