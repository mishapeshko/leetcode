class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        curr_sum = 0
        pom = {}
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum % k == 0:
                if i > 0:
                    return True
            if curr_sum%k in pom and pom[curr_sum%k] > 0:
                if pom[curr_sum%k] > 1:
                    return True
                else:
                    if nums[i]%k!=0:
                        return True
            if curr_sum%k in pom:
                pom[curr_sum%k] += 1
            else:   
                pom[curr_sum%k] = 1
        return False
            
