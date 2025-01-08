import math
N, D = map(int, input().split())
p = 2*D+1
ans = N / p
print(math.ceil(ans))