class Solution(object):
    def threeSumClosest(self, nums, target):
        n = len(nums)
        res = 100000
        nums = sorted(nums)
        ret = 0
        for k in range(1, n-1):
            i = 0
            j = n-1
            while(i < k and j > k):
                sum = nums[k]+nums[i]+nums[j]
                if abs(target-sum) < res:
                    res = abs(target-sum)
                    ret = sum
                if sum < target:
                    i += 1
                else:
                    j -= 1
        return ret
