from collections import OrderedDict

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        nextGreatElement = [0]*len(nums2)
        nextGreatElement[len(nums2)-1] = -1
        res = [0]*len(nums1)
        nums1H = OrderedDict()
        for num in nums1:
            nums1H[num] = 1
        nextEl = {}
        nextEl[nums2[len(nums2)-1]] = -1
        for j in range(len(nums2)-2, -1, -1):
            if nums2[j+1] > nums2[j]:
                nextGreatElement[j] = j+1
            else:
                i = j+1
                while(i != -1 and nums2[i] <= nums2[j]):
                    i = nextGreatElement[i]
                nextGreatElement[j] = i
            if nextGreatElement[j] == -1:
                nextEl[nums2[j]] = -1
            else:
                nextEl[nums2[j]] = nums2[nextGreatElement[j]]
        i = 0
        for item in nums1H:
            res[i] = nextEl[item]
            i += 1
        return res
