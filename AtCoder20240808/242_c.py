N = int(input())
prev = [1] * 9
curr = [0] * 9
p = 998244353

for i in range(1, N):
    for j in range(9):
        if j == 0:
            curr[j] = (prev[j] + prev[j + 1]) % p
        elif j == 8:
            curr[j] = (prev[j - 1] + prev[j]) % p
        else:
            curr[j] = (prev[j - 1] + prev[j] + prev[j + 1]) % p
    prev, curr = curr, [0] * 9  # prevを更新し、currをリセット

print(sum(prev) % p)