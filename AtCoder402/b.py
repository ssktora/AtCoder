Q = int(input())
customer = []
for i in range(Q):
    p = input().split()
    if p[0] == "1":
        X = p[1]
        customer.append(X)
    else:
        value = customer.pop(0)  
        print(value)
