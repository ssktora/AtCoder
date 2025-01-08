N = int(input())
A = list(map(int, input().split()))
p = 0
for a in A:
    p += (1/a)
ans = 1/p
print(ans)