N, K = map(int, input().split())
S = input()
import itertools

permutations = itertools.permutations(S)


S_set  = {''.join(p) for p in permutations}

p = 0
check = 0
for s in S_set:
    check += 1
    # print("-------")
    # print(s)
    for i in range(len(s)-K+1):
        string = s[i:i+K]
        #print(string)
        if string == string[::-1]:
            p += 1
            break
        
print(check-p)