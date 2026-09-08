from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        queue = deque()
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        pom = [[0 for j in range(cols)] for i in range(rows)]
        res = 10001
        ok = 1
        i = 0
        new_queue = deque()
        while(i < rows and ok == 1):
            j = 0
            while(j < cols and ok == 1):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    visited.add((i, j))
                    new_queue.append((i, j))
                    bfs(queue, visited, rows, cols, grid, new_queue)
                    ok = 0
                j += 1
            i += 1
        queue = new_queue
        while queue:
            row, col = queue.popleft()
            dist = pom[row][col]
            if row-1>=0 and (row-1, col) not in visited:
                visited.add((row-1, col))
                if grid[row-1][col] == 0:
                    pom[row-1][col] = dist+1
                    queue.append((row-1, col))
                else:
                    if dist < res:
                        res = dist
            if row+1<rows and (row+1, col) not in visited:
                visited.add((row+1, col))
                if grid[row+1][col] == 0:
                    pom[row+1][col] = dist+1
                    queue.append((row+1, col))
                else:
                    if dist < res:
                        res = dist
            if col-1>=0 and (row, col-1) not in visited:
                visited.add((row, col-1))
                if grid[row][col-1] == 0:
                    pom[row][col-1] = dist+1
                    queue.append((row, col-1))
                else:
                    if dist < res:
                        res = dist
            if col+1<cols and (row, col+1) not in visited:
                visited.add((row, col+1))
                if grid[row][col+1] == 0:
                    pom[row][col+1] = dist+1
                    queue.append((row, col+1))
                else:
                    if dist < res:
                        res = dist
        return res

def bfs(queue, visited, rows, cols, grid, new_queue):
    while queue:
        row, col = queue.popleft()
        if row-1>=0 and (row-1, col) not in visited and grid[row-1][col] == 1:
            visited.add((row-1, col))
            queue.append((row-1, col))
            new_queue.append((row-1, col))
        if row+1<rows and (row+1, col) not in visited and grid[row+1][col] == 1:
            visited.add((row+1, col))
            queue.append((row+1, col))
            new_queue.append((row+1, col))
        if col-1>=0 and (row, col-1) not in visited and grid[row][col-1] == 1:
            visited.add((row, col-1))
            queue.append((row, col-1))
            new_queue.append((row, col-1))
        if col+1<cols and (row, col+1) not in visited and grid[row][col+1] == 1:
            visited.add((row, col+1))
            queue.append((row, col+1))
            new_queue.append((row, col+1))
