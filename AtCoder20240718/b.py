N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0
pre = N+1
for i in A:
    if pre+1 == i:
        ans += B[i-1]+C[pre-1]
        pre = i
    else:
        ans += B[i-1]
        pre = i
print(ans)