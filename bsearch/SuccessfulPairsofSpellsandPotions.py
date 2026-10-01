class Solution(object):
    def successfulPairs(self, spells, potions, success):
        potions = sorted(potions)
        res = []
        for i in range(len(spells)):
            idx = bsearch(spells[i], potions, success)
            res.append(len(potions)-idx)
        return res

def bsearch(val, arr, target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = left + (right-left)//2
        if arr[mid]*val<target:
            left = mid+1
        else:
            right = mid-1
    return left
