S = list(input())
N = len(S)
ans = [0 for _ in range(N)]
for i in range(2):
    count = 0
    for i in range(N):
        if S[i] == "R":
            count += 1
        else:
            ans[i] += count//2
            ans[i-1] += (count+1)//2
            count = 0

    ans.reverse()
    S.reverse()
    for i in range(N):
        if S[i] == "L":
            S[i] = "R"
        else:
            S[i] = "L"

for i in range(len(ans)):
    ans[i] = str(ans[i])
print(" ".join(ans))
        