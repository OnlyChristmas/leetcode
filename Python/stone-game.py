'''
Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.



Example 1:

Input: [5,3,4,5]
Output: true
Explanation:
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.


Note:

2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles) is odd.
'''



class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        # Approach one  错误的动规思路，想错了最优子问题
        # A,B = 0,0
        # if piles :
        #     loc = piles.index(min(piles))
        #     B += piles.pop(loc)
        # while len(piles) > 1:
        #     if loc <= 0 or loc >=len(piles)-1:
        #         loc = piles.index(min(piles[0], piles[-1]))
        #         A += piles.pop(loc)
        #         if loc <= 0 or loc >= len(piles)-1:
        #             loc = piles.index(min(piles[0], piles[-1]))
        #             B += piles.pop(loc)
        #         else:
        #             loc = piles.index(min(piles[loc-1], piles[loc]))
        #             B += piles.pop(loc)
        #     else:
        #         loc = piles.index(min(piles[loc-1], piles[loc]))
        #         A += piles.pop(loc)
        #         if loc <= 0 or loc >= len(piles)-1:
        #             loc = piles.index(min(piles[0], piles[-1]))
        #             B += piles.pop(loc)
        #         else:
        #             loc = piles.index(min(piles[loc-1], piles[loc]))
        #             B += piles.pop(loc)
        # return (A + piles[0]) > B


        # Approach two
        A, B = 0,0
        while piles:
            if piles[0] >= piles[-1]:
                A += piles.pop(0)
                B += piles.pop(-1)
            else:
                A += piles.pop(-1)
                B += piles.pop(0)
        return A > B
