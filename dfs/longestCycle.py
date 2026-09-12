class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        res = [-1]
        visited = [0]*n
        for i in range(n):
            if visited[i] == 0:
                visitedH = {}
                stop = [False]
                dfs(visitedH, edges, i, 1, res, visited, stop)
        return res[0]

def dfs(visitedH, edges, start, idx, res, visited, stop):
    if stop[0]:
        return None
    visitedH[start] = idx
    visited[start] = 1
    if edges[start] == -1:
        stop[0] = True
        return None
    if edges[start] in visitedH:
        if idx-visitedH[edges[start]]+1 > res[0]:
            res[0] = idx-visitedH[edges[start]]+1
        stop[0] = True
        return None
    if visited[edges[start]] == 0:
        dfs(visitedH, edges, edges[start], idx+1, res, visited, stop)
