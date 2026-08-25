from dataclasses import dataclass
from collections import deque

@dataclass
class NodeData:
    string: str
    distance: int

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set()
        startData = NodeData(string = "0000", distance = 0)
        queue = deque()
        queue.append(startData)
        deadends = set(deadends)
        res = 10001
        while queue:
            element = queue.popleft()
            if element.string == target:
                if element.distance < res:
                    res = element.distance
            if element.string not in visited and element.string not in deadends:
                visited.add(element.string)
                newDistance = element.distance+1
                string1 = list(element.string)
                string1[3] = str((int(element.string[3])-1)%10)
                string1 = "".join(string1)
                string2 = list(element.string)
                string2[3] = str((int(element.string[3])+1)%10)
                string2 = "".join(string2)
                string3 = list(element.string)
                string3[2] = str((int(element.string[2])-1)%10)
                string3 = "".join(string3)
                string4 = list(element.string)
                string4[2] = str((int(element.string[2])+1)%10)
                string4 = "".join(string4)
                string5 = list(element.string)
                string5[1] = str((int(element.string[1])-1)%10)
                string5 = "".join(string5)
                string6 = list(element.string)
                string6[1] = str((int(element.string[1])+1)%10)
                string6 = "".join(string6)
                string7 = list(element.string)
                string7[0] = str((int(element.string[0])-1)%10)
                string7 = "".join(string7)
                string8 = list(element.string)
                string8[0] = str((int(element.string[0])+1)%10)
                string8 = "".join(string8)
                if string1 not in visited and string1 not in deadends:
                    queue.append(NodeData(string = string1, distance = newDistance))
                if string2 not in visited and string2 not in deadends:
                    queue.append(NodeData(string = string2, distance = newDistance))
                if string3 not in visited and string3 not in deadends:
                    queue.append(NodeData(string = string3, distance = newDistance))
                if string4 not in visited and string4 not in deadends:
                    queue.append(NodeData(string = string4, distance = newDistance))
                if string5 not in visited and string5 not in deadends:
                    queue.append(NodeData(string = string5, distance = newDistance))
                if string6 not in visited and string6 not in deadends:
                    queue.append(NodeData(string = string6, distance = newDistance))
                if string7 not in visited and string7 not in deadends:
                    queue.append(NodeData(string = string7, distance = newDistance))
                if string8 not in visited and string8 not in deadends:
                    queue.append(NodeData(string = string8, distance = newDistance))
        return -1 if res == 10001 else res
