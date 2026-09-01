class Solution(object):
    def topKFrequent(self, nums, k):
        n = len(nums)
        dictH = {}
        maxF = 1
        for num in nums:
            if num in dictH:
                dictH[num] += 1
                if dictH[num] > maxF:
                    maxF = dictH[num]
            else:
                dictH[num] = 1
        freq_num = [[] for i in range(maxF+1)]
        for num in dictH:
            freq_num[dictH[num]].append(num)
        counter = 0
        helper = 0
        res = []
        for i in range(maxF, 0, -1):
            if freq_num[i] != []:
                counter += i*len(freq_num[i])
                for j in range(len(freq_num[i])):
                    res.append(freq_num[i][j])
                helper += len(freq_num[i])
            if counter >= n or helper >= k:
                break
        return res
