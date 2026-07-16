from typing import List
#en i on achète et en j on vend
"""
Brut force : 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = float('-inf')
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]

                if profit > 0:
                    max_profit = max(max_profit, profit)
        return max_profit if max_profit > float('-inf') else 0

#Time : O(n²)
#Space : O(1)

==> Better idea :
use max_profit and min_price en bouclant une fois


"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time : O(n)
        # Space : O(1)
        min_price = float('inf')
        #ainsi si pas possible, on return direct 0
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
        return max_profit

