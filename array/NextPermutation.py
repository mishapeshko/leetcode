class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        if len(nums) == 1:
            return nums
        j = len(nums)-2
        while(j != -1 and nums[j] >= nums[j+1]):
            j -= 1
        cand = 101
        cand_j = -1
        i = j+1
        if j >= 0:
            while i < len(nums):
                if nums[i] <= cand and nums[i] > nums[j]:
                    cand = nums[i]
                    cand_j = i
                i += 1
            temp = nums[cand_j]
            nums[cand_j] = nums[j]
            nums[j] = temp
        i = j+1
        o = len(nums)-1
        while(i < o):
            nums[i], nums[o] = nums[o], nums[i]
            i += 1
            o -= 1
        return nums
