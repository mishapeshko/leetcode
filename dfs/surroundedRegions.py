class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            if board[i][0] == "O" and (i, 0) not in visited:
                visited.add((i, 0))
                dfs(visited, board, i, 0, rows, cols)
            if board[i][cols-1] == "O" and (i, cols-1) not in visited:
                visited.add((i, cols-1))
                dfs(visited, board, i, cols-1, rows, cols)
        for j in range(cols):
            if board[0][j] == "O" and (0, j) not in visited:
                visited.add((0, j))
                dfs(visited, board, 0, j, rows, cols)
            if board[rows-1][j] == "O" and (rows-1, j) not in visited:
                visited.add((rows-1, j))
                dfs(visited, board, rows-1, j, rows, cols)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (i, j) not in visited:
                    board[i][j] = "X"

def dfs(visited, board, row, col, rows, cols):
    if row-1>=0 and (row-1, col) not in visited and board[row-1][col] == "O":
        visited.add((row-1, col))
        dfs(visited, board, row-1, col, rows, cols)
    if row+1<rows and (row+1, col) not in visited and board[row+1][col] == "O":
        visited.add((row+1, col))
        dfs(visited, board, row+1, col, rows, cols)
    if col-1>=0 and (row, col-1) not in visited and board[row][col-1] == "O":
        visited.add((row, col-1))
        dfs(visited, board, row, col-1, rows, cols)
    if col+1<cols and (row, col+1) not in visited and board[row][col+1] == "O":
        visited.add((row, col+1))
        dfs(visited, board, row, col+1, rows, cols)
