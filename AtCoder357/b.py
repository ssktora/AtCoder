S = input()
small = 0
big = 0
for s in S:
    if s.islower():
        small += 1
    else:
        big += 1
if big > small:
    print(S.upper())
else:
    print(S.lower())
