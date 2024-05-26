N, T = map(int, input().split())
A = list(map(int, input().split()))
card = []
for i in range(N):
    line = []
    for j in range(N):
        n = N*i+j+1
        line.append(n)
    card.append(line)
print(card)
#for i in range(T):