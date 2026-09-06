from collections import deque
from dataclasses import dataclass

@dataclass
class QueueEntry:
    row: int
    col: int
    dist: int

class Solution(object):
    def updateMatrix(self, mat):
        queue = deque()
        rows = len(mat)
        cols = len(mat[0])
        res = [[0 for j in range(cols)] for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1:
                    res[i][j] = 10001
        visited = [set() for i in range(10001)]
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append(QueueEntry(i, j, 0))
        bfs(queue, res, visited, rows, cols, mat)
        return res

def bfs(queue, res, visited, rows, cols, mat):
    while queue:
        el = queue.popleft()
        curr_row = el.row
        curr_col = el.col
        curr_dist = el.dist+1
        if curr_row-1>=0 and mat[curr_row-1][curr_col] == 1 and (curr_row-1, curr_col) not in visited[curr_dist] and curr_dist < res[curr_row-1][curr_col]:
            visited[curr_dist].add((curr_row-1, curr_col))
            res[curr_row-1][curr_col] = curr_dist
            queue.append(QueueEntry(curr_row-1, curr_col, curr_dist))
        if curr_row+1<rows and mat[curr_row+1][curr_col] == 1 and (curr_row+1, curr_col) not in visited[curr_dist] and curr_dist < res[curr_row+1][curr_col]:
            visited[curr_dist].add((curr_row+1, curr_col))
            res[curr_row+1][curr_col] = curr_dist
            queue.append(QueueEntry(curr_row+1, curr_col, curr_dist))
        if curr_col-1>=0 and mat[curr_row][curr_col-1] == 1 and (curr_row, curr_col-1) not in visited[curr_dist] and curr_dist < res[curr_row][curr_col-1]:
            visited[curr_dist].add((curr_row, curr_col-1))
            res[curr_row][curr_col-1] = curr_dist
            queue.append(QueueEntry(curr_row, curr_col-1, curr_dist))
        if curr_col+1<cols and mat[curr_row][curr_col+1] == 1 and (curr_row, curr_col+1) not in visited[curr_dist] and curr_dist < res[curr_row][curr_col+1]:
            visited[curr_dist].add((curr_row, curr_col+1))
            res[curr_row][curr_col+1] = curr_dist
            queue.append(QueueEntry(curr_row, curr_col+1, curr_dist))          
