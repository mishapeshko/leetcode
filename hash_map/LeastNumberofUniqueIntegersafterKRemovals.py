class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = {}
        maxH = 0
        unique = 0
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
                unique += 1
            if freq[num] > maxH:
                maxH = freq[num]
        removals = [0]*(maxH+1)
        for num, score in freq.items():
            removals[score] += 1
        for i in range(1, maxH+1):
            if k>=i*removals[i]:
                k -= i*removals[i]
                unique -= removals[i]
            else:
                unique -= k//i
                k = 0
            if k == 0:
                break
        return unique
