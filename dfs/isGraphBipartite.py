class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = [0]*n
        states = [0]*n
        res = [True]
        for i in range(n):
            if visited[i] == 0:
                visitedH = {}
                dfs(graph, visited, visitedH, states, i, res, 1)
                if res[0] == False:
                    return False
        return res[0]

def dfs(graph, visited, visitedH, states, start, res, state):
    if not res[0]:
        return None
    visited[start] = 1
    visitedH[start] = 1
    states[start] = state
    for neighbour in graph[start]:
        if states[neighbour] != 0:
            if states[neighbour] % 2 == state % 2:
                res[0] = False
                return None
        if neighbour not in visitedH and visited[neighbour] == 0:
            dfs(graph, visited, visitedH, states, neighbour, res, state%2+1)
            if res[0] == False:
                return None
    del visitedH[start]
