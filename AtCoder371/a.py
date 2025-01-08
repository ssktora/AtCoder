a, b, c = map(str, input().split())
if a == "<":
    if b == "<":
        if c == "<":
            print("B")
        else:
            print("C")
    else:
        if c == "<":
            print("")
        else:
            print("A")
else:
    if b == "<":
        if c == "<":
            print("A")
        else:
            print("")
    else:
        if c == "<":
            print("C")
        else:
            print("B")
