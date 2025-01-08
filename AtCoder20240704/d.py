def add_child(tree, tree_count, parent, child):
    if parent not in tree:
        tree[parent] = []
        tree_count[parent] = 0
    tree[parent].append(child)
    if child not in tree:
        tree[child] = []
        tree_count[child] = 0

def add_count(tree, tree_count, parent, x):
    if parent in tree_count:
        tree_count[parent] += x
    if parent in tree:
        for c in tree[parent]:
            add_count(tree, tree_count, c, x)

# 使用例
tree = {}
tree_count = {}
N, Q = map(int, input().split())
for i in range(N-1):
    a, b = map(int, input().split())
    add_child(tree, tree_count, a, b)
for i in range(Q):
    p, x = map(int, input().split())
    add_count(tree, tree_count, p, x)

# 答えを準備する
ans = []
for i in range(1, N+1):
    ans.append(str(tree_count.get(i, 0)))

print(" ".join(ans))
