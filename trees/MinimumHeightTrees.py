class Solution(object):
    def findMinHeightTrees(self, n, edges):
        if(len(edges) == 0 and n == 1):
            return [0]
        neighbours = [set() for i in range(n)]
        leaves = set()
        for u, v in edges:
            neighbours[u].add(v)
            neighbours[v].add(u)
            if len(neighbours[u]) == 1:
                leaves.add(u)
            else:
                leaves.discard(u)
            if len(neighbours[v]) == 1:
                leaves.add(v)
            else:
                leaves.discard(v)
        curr = n
        while curr > 2:
            new_leaves = set()
            for leaf in leaves:
                for neighbour in neighbours[leaf]:
                    neighbours[neighbour].remove(leaf)
                    if len(neighbours[neighbour]) == 1:
                        new_leaves.add(neighbour)
                curr -= 1
            leaves = new_leaves
        return list(leaves)
