def is_valid_move(x, y, grid):
    # グリッドの範囲を超えていないか、壁や障害物がないかを確認
    return 0 < x <= len(grid) and 0 < y <= len(grid[0]) and grid[x-1][y-1] != '#'

def find_next_positions(current_x, current_y, grid, D):
    if D == "U":
        new_x, new_y = current_x - 1, current_y
        if is_valid_move(new_x, new_y, grid):
            return new_x, new_y
        else:
            return current_x, current_y 
    elif D == "D":
        new_x, new_y = current_x + 1, current_y
        if is_valid_move(new_x, new_y, grid):
            return new_x, new_y
        else:
            return current_x, current_y
    if D == "L":
        new_x, new_y = current_x, current_y -1
        if is_valid_move(new_x, new_y, grid):
            return new_x, new_y
        else:
            return current_x, current_y
    if D == "R":
        new_x, new_y = current_x, current_y + 1
        if is_valid_move(new_x, new_y, grid):
            return new_x, new_y
        else:
            return current_x, current_y
        
H, W, X, Y = map(int, input().split())
grid = [list(input()) for _ in range(H)]
#print(grid)
T = input()
count = 0
comes = set()
if grid[X-1][Y-1] == "@":
    count += 1
    comes.add((X,y))
for i in range(len(T)):
    d = T[i]
    pre_x, pre_y = X, Y
    X, Y = find_next_positions(pre_x,pre_y,grid,d)
    if grid[X-1][Y-1] == "@":
        if (X,Y) not in comes:
          count += 1
          comes.add((X,Y))
print(X,Y,count)
