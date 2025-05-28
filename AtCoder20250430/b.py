def is_valid_move(x, y, grid):
    if x == -1:
        return "N"
    elif x == len(grid):
        return "S"
    elif y == -1:
        return "W"
    elif y == len(grid[0]):
        return "E"
    else:
        return True

def find_next_positions(current_x, current_y, grid, direction):
    dx, dy = direction[0], direction[1]

    new_x, new_y = current_x + dx, current_y + dy

    if is_valid_move(new_x, new_y, grid):
        next_position = (new_x, new_y)
    else:
        if is_valid_move(new_x, new_y, grid) == "N":
            next_position = (len(grid)-1, current_y)
        elif is_valid_move(new_x, new_y, grid) == "E":
            next_position = (current_x, 0)
        elif is_valid_move(new_x, new_y, grid) == "S":
            next_position = (0, current_y)
        else:
            next_position = (current_x, len(grid[0])-1)
    return next_position


    return next_positions
H, W, N = map(int, input().split())
grid = ["."*W for _ in range(H)]
now = (0,0)
direction = (-1,0)
for i in range(N):
    mass = grid[now[0]][now[1]]
    if mass == ".":
        grid[now[0]][now[1]] = "#"
        if direction == (-1,0):
            direction = (0,1)
            now = find_next_positions(now[0], now[1], grid, direction)
        elif direction == (0,1):
            direction = (1,0)
            now = find_next_positions(now[0], now[1], grid, direction)
        elif direction == (1,0):
            direction = (0,-1)
            now = find_next_positions(now[0], now[1], grid, direction)
        else:
            direction = (-1,0)
            now = find_next_positions(now[0], now[1], grid, direction)
    else:
        grid[now[0]][now[1]] = "."
        if direction == (-1,0):
            direction = (0,-1)
            now = find_next_positions(now[0], now[1], grid, direction)
        elif direction == (0,-1):
            direction = (1,0)
            now = find_next_positions(now[0], now[1], grid, direction)
        elif direction == (1,0):
            direction = (0,1)
            now = find_next_positions(now[0], now[1], grid, direction)
        else:
            direction = (-1,0)
            now = find_next_positions(now[0], now[1], grid, direction)

for i in range(len(grid)):
    print(grid[i])



