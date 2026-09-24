"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        dictH = {}
        counter = 0
        n = lenH(head)
        curr = head
        prev = None
        helpH = 0
        newH = None
        while(counter < n):
            newN = newNode(curr.val)
            if helpH == 0:
                helpH = 1
                newH = newN
            dictH[curr] = newN
            counter += 1
            curr = curr.next
            if prev:
                prev.next = newN
            prev = newN
        counter = 0
        curr = head
        while(counter < n):
            if curr.random != None:
                dictH[curr].random = dictH[curr.random]
            else:
                dictH[curr].random = None
            curr = curr.next
            counter += 1
        return newH
    
def newNode(value):
    return Node(value, None, None)
    
def lenH(head):
    res = 0
    while(head):
        head = head.next
        res += 1
    return res
