import math
X = int(input())
i = 1
while True:
    p = math.factorial(i)
    if p == X:
        print(i)
        break
    i += 1
