from itertools import permutations

def generate_substrings(S, K):
    substrings = set()
    for i in range(len(S) - K + 1):
        substrings.add(S[i:i + K])
    return substrings

def is_palindrome(s):
    return s == s[::-1]

def check(N, K, S):
    seen = set()
    ans = 0
    palindrome_memo = {}

    # すべての部分文字列を生成
    substrings = generate_substrings(S, K)
    for substr in substrings:
        palindrome_memo[substr] = is_palindrome(substr)

    for perm in permutations(S):
        perm_str = ''.join(perm)
        if perm_str not in seen:
            if not any(palindrome_memo[perm_str[i:i + K]] for i in range(len(perm_str) - K + 1)):
                seen.add(perm_str)
                ans += 1

    return ans

# 入力の取得
N, K = map(int, input().split())
S = input()

# 結果の出力
print(check(N, K, S))

    
