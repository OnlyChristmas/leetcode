'''

Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.

Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.


Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

'''




class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # method one
#        考虑特殊情况空列表, 效率低 O(n^2)
        # return max([max(prices[i:])-prices[i] for i in range(len(prices))])  if prices else 0


        # method two  还是效率低
        # res = 0
        # while prices:
        #     max_price = max(prices)
        #     tmp = max_price - min(prices[:prices.index(max_price)+1])
        #     if tmp < res:
        #         return res
        #     else:
        #         res = tmp
        #     prices.remove(max_price)
        # return 0



        # method three  O(n) ，空间复杂度1 ，不用冗余的max()操作
        profit , min_price = 0 , float('inf')
        for price in prices:
            profit = max(price - min_price , profit)
            min_price = min(price , min_price)
        return profit
