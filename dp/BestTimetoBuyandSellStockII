class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [0]*n
        nextSmaller = [-1]*n
        for i in range(1, n):
            if prices[i-1] < prices[i]:
                nextSmaller[i] = i-1
            else:
                j = i-1
                while prices[j] >= prices[i] and j != -1:
                    j = nextSmaller[j]
                nextSmaller[i] = j
        dp[0] = 0
        for i in range(1, n):
            res = 0
            j = nextSmaller[i]
            while(j != -1):
                if j-1>=0:
                    res = max(res, prices[i]-prices[j]+dp[j-1])
                else:
                    res = max(res, prices[i]-prices[j])
                j = nextSmaller[j]
            dp[i] = max(res, dp[i-1])
        return dp[n-1]
