class Solution(object):
    def minIncrementForUnique(self, nums):
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        res = 0
        keys = sorted(freq.keys())
        curr = keys[0]
        stack = []
        for key in keys:
            while stack and curr < key:
                item = stack.pop()
                res += curr - item
                curr += 1
            for i in range(freq[key]-1):
                stack.append(key)
            curr = key+1
        while stack:
            item = stack.pop()
            res += curr-item
            curr += 1
        return res
