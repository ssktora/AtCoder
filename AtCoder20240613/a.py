A, B = map(int, input().split())
P = abs(A-B)
if P % 2 == 0:
    if A < B:
      print(int(A+P/2))
    else:
      print(int(B+P/2))
else:
    print("IMPOSSIBLE")