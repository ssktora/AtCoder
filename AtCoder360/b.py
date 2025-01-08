S, T = map(str, input().split())
for w in range(1,len(S)):
    s = [S[i:i+w] for i in range(0, len(S), w)]
    n = len(s[-1])
    for c in range(len(w)):
        result = ""
        if c+1 <= n:
            for j in range(len(s)):
                result += s[c][j]
            if result == T:
                frag = False
                print("Yes")
                exit
        else:
            for j in range(len(s)-1):
                result += s[c][j]
            if result == T:
                frag = False
                print("Yes")
                exit
if frag:
    print("No")