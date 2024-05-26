A,B = map(int, input().split())
if A == B:
    print(-1)
else:
    check = {1,2,3}
    p = {A,B}
    ans = check-p
    for a in ans:
        print(a)