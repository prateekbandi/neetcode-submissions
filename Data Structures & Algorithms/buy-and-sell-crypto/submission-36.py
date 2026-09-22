class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        left, right = 0, 1

        while right < len(prices):
            profit = prices[right] - prices[left]
            maxP = max(maxP, profit)

            while prices[left] > prices[right]:
                left += 1
            right += 1
        return maxP
        