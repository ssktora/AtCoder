N, M = map(int, input().split())
S = input()
def split_by_zero(s: str) -> list[str]:
    return [part for part in s.split('0') if part]
S_list = split_by_zero(S)
ans = -1
for s in S_list:
    one = s.count("1")
    two = s.count("2")
    if one > M:
       p = (one-M)+two
    else:
       p = two
    ans = max(ans,p)

print(ans)

    