class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0 for i in range(cols)] for j in range(rows)]
        act = 0
        for i in range(rows):
            for j in range(cols):
                if dp[i][j] == 0:
                    res = [1]
                    visited = set()
                    dfs(matrix, visited, i, j, res, rows, cols, dp)
                if dp[i][j] > act:
                    act = dp[i][j]
        return act

def dfs(matrix, visited, row, col, res, rows, cols, dp):
    if dp[row][col] != 0:
        res[0] = dp[row][col]
        return None
    visited.add((row, col))
    pom = [1]
    pomH = [1]
    if row-1>=0 and dp[row-1][col] == 0:
        if (row-1, col) not in visited and matrix[row-1][col] > matrix[row][col]:
            dfs(matrix, visited, row-1, col, pom, rows, cols, dp)
            if pom[0]+1 > pomH[0]:
                pomH[0] = pom[0]+1
    else:
        if row-1>=0:
            if matrix[row-1][col] > matrix[row][col]:
                if pomH[0] < dp[row-1][col]+1:
                    pomH[0] = dp[row-1][col]+1
    if row+1 < rows and dp[row+1][col] == 0:
        if (row+1, col) not in visited and matrix[row+1][col] > matrix[row][col]:
            dfs(matrix, visited, row+1, col, pom, rows, cols, dp)
            if pom[0]+1 > pomH[0]:
                pomH[0] = pom[0]+1
    else:
        if row+1<rows:
            if matrix[row+1][col] > matrix[row][col]:
                if pomH[0] < dp[row+1][col]+1:
                    pomH[0] = dp[row+1][col]+1
    if col-1>=0 and dp[row][col-1] == 0:
        if (row, col-1) not in visited and col-1>=0 and matrix[row][col-1] > matrix[row][col]:
            dfs(matrix, visited, row, col-1, pom, rows, cols, dp)
            if pom[0]+1 > pomH[0]:
                pomH[0] = pom[0]+1
    else:
        if col-1>=0:
            if matrix[row][col-1] > matrix[row][col]:
                if pomH[0] < dp[row][col-1]+1:
                    pomH[0] = dp[row][col-1]+1
    if col+1<cols and dp[row][col+1] == 0:
        if (row, col+1) not in visited and col+1<cols and matrix[row][col+1] > matrix[row][col]:
            dfs(matrix, visited, row, col+1, pom, rows, cols, dp)
            if pom[0]+1 > pomH[0]:
                pomH[0] = pom[0]+1
    else:
        if col+1<cols:
            if matrix[row][col+1] > matrix[row][col]:
                if pomH[0] < dp[row][col+1]+1:
                    pomH[0] = dp[row][col+1]+1
    res[0] = pomH[0]
    dp[row][col] = res[0]
    visited.remove((row, col))
