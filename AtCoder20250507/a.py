N = int(input())
rest = [i for i in range(0,101,5)]
ans = 10000000000000
ans_i = 0
for i in range(len(rest)):
    p = abs(N-rest[i])
    if ans > p:
        ans = p
        ans_i = i

print(rest[ans_i])