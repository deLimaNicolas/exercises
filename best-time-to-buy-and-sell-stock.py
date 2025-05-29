#You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
#
#You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
#
#Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.
#
#Example 1:
#       lastProfit = 7
#       buy = 1
#       sell = 3
#Input: prices = [10,2,5,6,7,1]
#
#Output: 6
#Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.
#
#Example 2:
#
#Input: prices = [10,8,7,5,2]
#
#Output: 0
#Explanation: No profitable transactions can be made, thus the max profit is 0.
#
#Constraints:
#
#1 <= prices.length <= 100
#0 <= prices[i] <= 100
#

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1

        pricesLen = len(prices)

        ans = 0

        if not prices:
            return ans

        if pricesLen == 1:
            return 0
        while right < pricesLen:
            if prices[left] < prices[right]:
                ans = max(prices[right] - prices[left], ans)
                right += 1
            else:
                left = right
                right += 1
        return ans

def main():
    solution = Solution()
    print(solution.maxProfit([10,2,5,6,7,1]))

main()
