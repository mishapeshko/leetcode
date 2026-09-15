class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        isCycle = [0]*n
        visited = [0]*n
        for i in range(n):
            if visited[i] == 0:
                visitedH = set()
                cycle = [False]
                dfs(graph, visited, visitedH, isCycle, i, cycle)
        res = []
        for i in range(n):
            if isCycle[i] == 0:
                res.append(i)
        return res

def dfs(graph, visited, visitedH, isCycle, start, cycle):
    visited[start] = 1
    visitedH.add(start)
    if isCycle[start] == 1:
        cycle[0] = True
        return None
    cycleH = [False]
    for neighbour in graph[start]:
        if cycleH[0] == True:
            break
        if isCycle[neighbour] == 1:
            cycleH[0] = True
        else:
            if neighbour in visitedH:
                cycleH[0] = True
            else:
                if visited[neighbour] == 0:
                    dfs(graph, visited, visitedH, isCycle, neighbour, cycleH)
    if cycleH[0]:
        isCycle[start] = 1
    cycle[0] = cycleH[0]
    visitedH.remove(start)
