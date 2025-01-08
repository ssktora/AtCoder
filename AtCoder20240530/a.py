N, A, B = map(int, input().split())
train = N*A
if train >= B:
    print(B)
else:
    print(train)