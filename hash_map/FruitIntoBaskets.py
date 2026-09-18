class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        unique = 0
        left = 0
        dictH = {}
        res = 0
        right = 0
        while right < len(fruits):
            while unique <= 2 and right < len(fruits):
                if fruits[right] not in dictH:
                    unique += 1
                    dictH[fruits[right]] = 1
                    if unique == 3:
                        if right - left > res:
                            res = right-left
                else:
                    dictH[fruits[right]] += 1
                if unique <= 2:
                    if right-left+1 > res:
                        res = right-left+1
                right += 1
            stop = False
            while unique > 2 and stop == False:
                dictH[fruits[left]] -= 1
                if dictH[fruits[left]] == 0:
                    unique -= 1
                    stop = True
                    del dictH[fruits[left]]
                left += 1
        return res
