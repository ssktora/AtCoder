Q = int(input())
sneaks = []
cumsum = []  

for i in range(Q):
    q = input()
    if q[0] == "1":
        _, l = map(int, q.split())
        sneaks.append(l)
        if cumsum:
            cumsum.append(cumsum[-1] + l)
        else:
            cumsum.append(l) 
    elif q[0] == "2":
        if sneaks:
            removed = sneaks.pop(0)
            cumsum = [x - removed for x in cumsum[1:]]
    else:
        _, k = map(int, q.split())
        if 0 <= k-1 < len(cumsum):
            print(cumsum[k-1])

