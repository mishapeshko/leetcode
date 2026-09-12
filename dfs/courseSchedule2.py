class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = [True]
        neighbours = [[] for i in range(numCourses)]
        for u, v in prerequisites:
            neighbours[u].append(v)
        visitedH = [0]*numCourses
        visited = [0]*numCourses
        for i in range(numCourses):
            if visited[i] == 0:
                dfs(neighbours, res, visited, visitedH, i)
        fin = [0]*numCourses
        if res[0] == False:
            return []
        idx = [0]
        visited = [0]*numCourses
        dictH = set()
        for i in range(numCourses):
            if visited[i] == 0:
                topo(neighbours, idx, i, fin, visited, dictH)
        for j in range(numCourses):
            if j not in dictH:
                fin[idx[0]] = j
                idx[0] += 1
        return fin

def topo(neighbours, idx, start, fin, visited, dictH):
    if visited[start] == 1:
        return None
    visited[start] = 1
    dictH.add(start)
    for neighbour in neighbours[start]:
        if visited[neighbour] == 0:
            topo(neighbours, idx, neighbour, fin, visited, dictH)
    fin[idx[0]] = start
    idx[0] += 1

def dfs(neighbours, res, visited, visitedH, start):
    if res[0] == False:
        return None
    visited[start] = 1
    visitedH[start] = 1
    for neighbour in neighbours[start]:
        if visitedH[neighbour] == 1:
            res[0] = False
            return None
        if visited[neighbour] == 0:
            dfs(neighbours, res, visited, visitedH, neighbour)
    visitedH[start] = 0
