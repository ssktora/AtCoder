N = int(input())
S = input()
takahahshi = 0
aoki = 0
for i in range(N):
    if S[i] == 'T':
        takahahshi += 1
    else:
        aoki += 1
if takahahshi > aoki:
    print("T")
elif aoki > takahahshi:
    print("A")
else:
    if S[-1] == 'T':
        print("A")
    else:
        print("T")