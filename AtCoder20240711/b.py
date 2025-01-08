A, B = map(int, input().split())
for i in range(100):
    not_used = (A*i+1)-i
    if not_used >= B:
        print(i)
        break