N, Q = map(int, input().split())
x_list = []
for i in range(Q):
    x = int(input())
    x_list.append(x)

pos = [i for i in range(1,N+1)]
index_of = {}
for i in range(1,N+1):
    index_of[i] = i-1

for x in x_list:
    i = index_of[x]
    if i == N-1:
        j = i-1
    else:
        j = i+1
    a,b = pos[i],pos[j]
    pos[i],pos[j] = b,a
    index_of[a],index_of[b] =j,i

print(" ".join(map(str,pos)))