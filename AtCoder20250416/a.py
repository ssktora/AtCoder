N, S, K = map(int, input().split())
price = 0
for i in range(N):
    p, q = map(int, input().split())
    price += p*q

if price < S:
    print(price+K)
else:
    print(price)
