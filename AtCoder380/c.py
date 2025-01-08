N, K = map(int, input().split())
S = input()
s_list = []
p = 0
st = S[0]
pre = S[0]
frag = True
for s in S[1:]:
    if s == pre:
        st += s
    else:
        if st[0] == "1":
            p += 1
        s_list.append(st)
        if p == K and frag:
            s_list[-1], s_list[-2] = s_list[-2], s_list[-1]
            frag = False
        st = s
        pre = s
if st[0] == "1":
    p += 1
s_list.append(st)
if p == K and frag:
    s_list[-1], s_list[-2] = s_list[-2], s_list[-1]
    frag = False

print("".join(s_list))