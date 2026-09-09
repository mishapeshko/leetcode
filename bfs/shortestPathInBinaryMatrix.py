from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        pom = [[1 for j in range(cols)] for i in range(rows)]
        queue.append((0,0))
        visited = set()
        visited.add((0,0))
        while queue:
            row, col = queue.popleft()
            dist = pom[row][col]
            if row-1>=0 and col-1>=0 and (row-1, col-1) not in visited and grid[row-1][col-1] == 0:
                visited.add((row-1, col-1))
                pom[row-1][col-1] = dist+1
                queue.append((row-1, col-1))
            if row-1>=0 and (row-1, col) not in visited and grid[row-1][col] == 0:
                visited.add((row-1, col))
                pom[row-1][col] = dist+1
                queue.append((row-1, col))
            if row-1>=0 and col+1<cols and (row-1, col+1) not in visited and grid[row-1][col+1] == 0:
                visited.add((row-1, col+1))
                pom[row-1][col+1] = dist+1
                queue.append((row-1, col+1))
            if col-1>=0 and (row, col-1) not in visited and grid[row][col-1] == 0:
                visited.add((row, col-1))
                pom[row][col-1] = dist+1
                queue.append((row, col-1))
            if col+1<cols and (row, col+1) not in visited and grid[row][col+1] == 0:
                visited.add((row, col+1))
                pom[row][col+1] = dist+1
                queue.append((row, col+1))
            if row+1<rows and col-1>=0 and (row+1, col-1) not in visited and grid[row+1][col-1] == 0:
                visited.add((row+1, col-1))
                pom[row+1][col-1] = dist+1
                queue.append((row+1, col-1))
            if row+1<rows and (row+1, col) not in visited and grid[row+1][col] == 0:
                visited.add((row+1, col))
                pom[row+1][col] = dist+1
                queue.append((row+1, col))
            if row+1<rows and col+1<cols and (row+1, col+1) not in visited and grid[row+1][col+1] == 0:
                visited.add((row+1, col+1))
                pom[row+1][col+1] = dist+1
                queue.append((row+1, col+1))
        if pom[rows-1][cols-1] == 1:
            if rows != 1:
                return -1
            else:
                if grid[rows-1][cols-1] == 0:
                    return 1
                else:
                    return -1
        return pom[rows-1][cols-1]
