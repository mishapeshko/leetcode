from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        res = [0]
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    visited.add((i, j))
        pom = [[0 for j in range(cols)] for i in range(rows)]
        bfs(queue, rows, cols, res, pom, visited, grid)
        if res[0] > 0:
            return res[0]
        return -1

def bfs(queue, rows, cols, res, pom, visited, grid):
    while queue:
        row, col = queue.popleft()
        dist = pom[row][col]
        if dist > res[0]:
            res[0] = dist
        if row-1>=0 and (row-1, col) not in visited:
            visited.add((row-1, col))
            pom[row-1][col] = dist+1
            queue.append((row-1, col))
        if row+1<rows and (row+1, col) not in visited:
            visited.add((row+1, col))
            pom[row+1][col] = dist+1
            queue.append((row+1, col)) 
        if col-1>=0 and (row, col-1) not in visited:
            visited.add((row, col-1))
            pom[row][col-1] = dist+1
            queue.append((row, col-1)) 
        if col+1<cols and (row, col+1) not in visited:
            visited.add((row, col+1))
            pom[row][col+1] = dist+1
            queue.append((row, col+1))
