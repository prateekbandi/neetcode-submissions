class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxP = 0

        while right < len(prices):
            profit = prices[right] - prices[left]
            maxP = max(maxP, profit)

            while prices[right] < prices[left]:
                left += 1
            right += 1
        return maxP
        