class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        dictH = {}
        act = 0
        right = 0
        n = len(nums)
        if k > n:
            return 0
        res = 0
        while(right < n):
            if right-left+1>k:
                act = 0
                del dictH[nums[left]]
                left += 1
            if right-left+1==k:
                if nums[right] in dictH and dictH[nums[right]] >= left:
                    act += nums[right]
                    for j in range(left, dictH[nums[right]]):
                        act -= nums[j]
                        del dictH[nums[j]]
                    act -= nums[right]
                    left = dictH[nums[right]]+1
                else:
                    act += nums[right]
                    if act > res:
                        res = act
                    act -= nums[left]
                    left += 1
            else:
                if nums[right] in dictH and dictH[nums[right]] >= left:
                    act += nums[right]
                    for j in range(left, dictH[nums[right]]):
                        act -= nums[j]
                        del dictH[nums[j]]
                    act -= nums[right]
                    left = dictH[nums[right]]+1
                else:
                    act += nums[right]
            dictH[nums[right]] = right
            right += 1
        return res
