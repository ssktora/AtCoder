H, W = map(int, input().split())
S = [input() for _ in range(H)]
dp = [[0 for _ in range(W)] for _ in range(H)]
def is_valid_move(x, y, grid):
    # グリッドの範囲を超えていないか、壁や障害物がないかを確認
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != '#'

def find_next_positions(current_x, current_y, grid):
    directions = [(0, 1), (1, 0)] 

    next_positions = []

    for dx, dy in directions:
        new_x, new_y = current_x + dx, current_y + dy

        if is_valid_move(new_x, new_y, grid):
            next_positions.append((new_x, new_y))

    return next_positions
for i in range(H-1,-1,-1):
    for j in range(W-1,-1,-1):
        if S[i][j] == ".":
            next = find_next_positions(i,j,S)
            if len(next) == 0:
                dp[i][j] = 1
            else:
                max_p = 0
                for k in range(len(next)):
                    x = next[k][0]
                    y = next[k][1]
                    max_p = max(max_p,dp[x][y])
                dp[i][j] = max_p+1
print(dp[0][0])