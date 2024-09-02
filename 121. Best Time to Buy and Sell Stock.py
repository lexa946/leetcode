from typing import List



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for i in range(len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            elif min_price < prices[i]:
                profit = prices[i] - min_price
                if profit > max_profit:
                    max_profit = profit


        return max_profit




sol = Solution()
print(sol.maxProfit(prices = [2,4,1]))
print(sol.maxProfit(prices = [7,1,5,3,6,4]))
print(sol.maxProfit(prices = [3,2,6,5,0,3]))
assert sol.maxProfit(prices = [2,1,2,0,1]) == 1