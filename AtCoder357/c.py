

def create_grid(N):
    if N == 1:
        return [["#", "#", "#"], ["#", ".", "#"], ["#", "#", "#"]]
    
    smaller_grid = create_grid(N-1)
    # リスト内の全ての要素を「.」に置き換える
    center = [['.' for _ in row] for row in smaller_grid]
    return [[smaller_grid, smaller_grid, smaller_grid], [smaller_grid, center, smaller_grid], [smaller_grid, smaller_grid, smaller_grid]]

def format_grid(grid):
    formatted_grid = []
    for row in grid:
        formatted_row = []
        for subgrid in row:
            if isinstance(subgrid, str):
                formatted_row.append(subgrid)
            else:
                for subrow in subgrid:
                    formatted_row.append(''.join(subrow))
        formatted_grid.append(''.join(formatted_row))
    return '\n'.join(formatted_grid)


N = int(input())
grid = create_grid(N)
# グリッドを文字列に変換して表示
ans = format_grid(grid)
#print(ans)