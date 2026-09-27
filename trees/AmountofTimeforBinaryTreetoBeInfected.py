from collections import deque

class Node(object):
    def __init__(self, val, left, right, parent, dist):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.dist = dist

class Solution(object):
    def amountOfTime(self, root, start):
        rootNew = copyTree(root, None)
        startt = [None]
        nodeStart(rootNew, start, startt)
        queue = deque()
        startt[0].dist = 0
        visited = set()
        visited.add(startt[0])
        queue.append(startt[0])
        res = 0
        while queue:
            el = queue.popleft()
            if el.dist > res:
                res = el.dist
            if el.left != None and el.left not in visited:
                el.left.dist = el.dist+1
                visited.add(el.left)
                queue.append(el.left)
            if el.right != None and el.right not in visited:
                el.right.dist = el.dist+1
                visited.add(el.right)
                queue.append(el.right)
            if el.parent != None and el.parent not in visited:
                el.parent.dist = el.dist+1
                visited.add(el.parent)
                queue.append(el.parent)
        return res
    
def nodeStart(root, start, startt):
    if not root or startt[0] != None:
        return None
    if root.val == start:
        startt[0] = root
    nodeStart(root.left, start, startt)
    nodeStart(root.right, start, startt)

def copyTree(root, parent):
    if not root:
        return None
    node = Node(root.val, None, None, parent, -1)
    node.left = copyTree(root.left, node)
    node.right = copyTree(root.right, node)
    return node
