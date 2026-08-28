class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        n = numCourses
        visited = [False]*n
        neighbours = [[] for i in range(n)]
        setP = set()
        for u, v in prerequisites:
            neighbours[u].append(v)
            setP.add(u)
        odp = [True]
        for i in range(n):
            if not visited[i]:
                if i in setP:
                    visitedNow = {}
                    visitedNow[i] = 1
                    visited[i] = True
                    visit(neighbours, visited, i, odp, visitedNow)
        return odp[0]

def visit(neighbours, visited, nr, odp, visitedNow):
    for u in neighbours[nr]:
        if u in visitedNow:
            odp[0] = False
            return None
        if visited[u]:
            return None
        visitedNow[u] = 1
        visited[u] = True
        visit(neighbours, visited, u, odp, visitedNow)
        del visitedNow[u]
