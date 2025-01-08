H, W = map(int, input().split())
current_x,current_y = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(H)]
X = input()

def is_valid_move(x, y, grid):
    # グリッドの範囲を超えていないか、壁や障害物がないかを確認
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != '#'

def find_next_positions(current_x, current_y, grid, d):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 北、南、東、西
    if d == "L" :
        new_x, new_y = current_x, current_y-1
    elif d == "U":
        new_x, new_y = current_x-1, current_y
    elif d == "R":
        new_x, new_y = current_x, current_y+1
    elif d == "D":
        new_x, new_y = current_x+1, current_y


    if is_valid_move(new_x, new_y, grid):
        x,y = new_x,new_y
    else:
        x,y = current_x,current_y

    return x,y

for i in range(len(X)):
    d = X[i]
    current_x,current_y = find_next_positions(current_x, current_y, S, d)

print(current_x,current_y)
    
