S = input()
N = len(S) 
grid = [1 for _ in range(N)]
p3 = ["RRR", "RRL", "RLR", "RLL", "LLR", "LLL", "LRR", "LRL"]
n3 = ["111", "110", "101", "100", "001", "000", "011", "010"]
for p in p3:
    for n in n3:
        a = int(n[1])
        if p[0] == "R" and p[2] == "R":
            if n[0] != "0"

count = 0
for i in range(N):
    if i == 0:
        if S[1] == "L":
            if grid[0] == 0:
                grid[0] += 1 
        else:
            if grid[0] != 0:
                grid[0] -= 1
    elif i == N-1:
        if S[-2] == "L":
            if grid[-1] != 0:
                grid[-1] -= 1 
        else:
            if grid[-1] == 0:
                grid[-1] += 1
    else:


