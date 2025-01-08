X = input()
ans = []
zero = []
for x in X:
    if x == "0":
        zero.append("0")
    else:
        ans += zero
        zero = []
        ans.append(x)
if ans[-1] == ".":
    ans.pop(-1)
print("".join(ans))