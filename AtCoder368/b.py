N = int(input())
A = list(map(int, input().split()))

def check(a_list):
    count = 0
    for a in a_list:
        if a > 0:
            count += 1
    if count <= 1:
        return True
    else:
        return False

ans = 1
while True:
    A = sorted(A, reverse=True)
    A[0] -= 1
    A[1] -= 1
    if check(A):
        break
    else:
        ans += 1

print(ans)
