class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        for i in range(rows):
            if grid[i][0] == 0 and (i, 0) not in visited:
                visited.add((i, 0))
                dfs(visited, grid, rows, cols, i, 0)
            if grid[i][cols-1] == 0 and (i, cols-1) not in visited:
                visited.add((i, cols-1))
                dfs(visited, grid, rows, cols, i, cols-1)
        for i in range(cols):
            if grid[0][i] == 0 and (0, i) not in visited:
                visited.add((0, i))
                dfs(visited, grid, rows, cols, 0, i)
            if grid[rows-1][i] == 0 and (rows-1, i) not in visited:
                visited.add((rows-1, i))
                dfs(visited, grid, rows, cols, rows-1, i)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0 and (i, j) not in visited:
                    visited.add((i, j))
                    dfs(visited, grid, rows, cols, i, j)
                    res += 1
        return res

def dfs(visited, grid, rows, cols, row, col):
    if row-1>=0 and (row-1, col) not in visited and grid[row-1][col] == 0:
        visited.add((row-1, col))
        dfs(visited, grid, rows, cols, row-1, col)
    if row+1<rows and (row+1, col) not in visited and grid[row+1][col] == 0:
        visited.add((row+1, col))
        dfs(visited, grid, rows, cols, row+1, col)
    if col-1>=0 and (row, col-1) not in visited and grid[row][col-1] == 0:
        visited.add((row, col-1))
        dfs(visited, grid, rows, cols, row, col-1)
    if col+1<cols and (row, col+1) not in visited and grid[row][col+1] == 0:
        visited.add((row, col+1))
        dfs(visited, grid, rows, cols, row, col+1)
