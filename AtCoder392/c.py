N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
wear = {}
weared = {}
look = {}
looked = {}
for i in range(N):
    wear[i+1] = Q[i]
    weared[Q[i]] = i+1
    look[i+1] = P[i]
    looked[P[i]] = i+1
S = []
for i in range(N):
    target = weared[i+1]
    ans_target = look[target]
    p = wear[ans_target]
    S.append(str(p))

print(" ".join(S))
