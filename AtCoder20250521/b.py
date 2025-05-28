N = int(input())
while True:
    p = str(N)
    if int(p[-3])*int(p[-2]) == int(p[-1]):
        print(N)
        break
    else:
        N += 1

