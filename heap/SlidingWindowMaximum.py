from dataclasses import dataclass

@dataclass
class HeapItem:
    queueNum: int
    val: int

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        res = []
        dictH = {}
        left = 0
        heap = [0]*k
        size = 0
        for right in range(len(nums)):
            if right < k:
                heap[size] = HeapItem(right, nums[right])
                dictH[right] = size
                heapifyUp(dictH, heap, size)
                size += 1
            else:
                res.append(heap[0].val)
                idx_left = dictH[left]
                del dictH[left]
                new_Entry = HeapItem(right, nums[right])
                old_parent = 0
                if idx_left >= 1:
                    old_parent = heap[(idx_left-1)//2].val
                else:
                    old_parent = heap[0].val
                heap[idx_left] = new_Entry
                dictH[right] = idx_left
                if nums[right] > old_parent:
                    heapifyUp(dictH, heap, idx_left)
                else:
                    heapifyDown(dictH, heap, idx_left, k)
                left += 1
        res.append(heap[0].val)
        return res
            
def heapifyUp(dictH, heap, idx):
    if idx == 0:
        return None
    else:
        parent = (idx-1)//2
        if heap[parent].val < heap[idx].val:
            dictH[heap[parent].queueNum] = idx
            dictH[heap[idx].queueNum] = parent
            temp = heap[parent]
            heap[parent] = heap[idx]
            heap[idx] = temp
            heapifyUp(dictH, heap, (idx-1)//2)
        return None

def heapifyDown(dictH, heap, idx, k):
    if idx >= k:
        return None
    else:
        left_child = 2*idx+1
        right_child = 2*idx+2
        largest = idx
        if left_child < k and heap[left_child].val > heap[idx].val:
            largest = left_child
        if right_child < k and heap[right_child].val > heap[largest].val:
            largest = right_child
        if largest != idx:
            dictH[heap[idx].queueNum] = largest
            dictH[heap[largest].queueNum] = idx
            temp = heap[idx]
            heap[idx] = heap[largest]
            heap[largest] = temp
            heapifyDown(dictH, heap, largest, k)
        return None
