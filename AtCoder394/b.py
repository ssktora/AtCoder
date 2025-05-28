N = int(input())
s_list = []
for i in range(N):
    s = input()
    n = len(s)
    s_list.append((n,s))
s_list = sorted(s_list)
ans = ""
for s in s_list:
    ans += s[1]
print(ans)