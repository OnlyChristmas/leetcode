'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.





The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.



Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49

'''



class Solution:
    def maxArea(self, height: 'List[int]') -> 'int':
        # Approach one  TLE
        # l,r = 0,1
        # res = 0
        # length = len(height)
        # while l < length - 1:
        #     new_res = min(height[r] , height[l]) * (r - l)
        #     if new_res > res:
        #         res = new_res
        #     else:
        #         r += 1
        #         if r >= length:
        #             l += 1
        #             r = l + 1
        # return res



        # Approach two  撞指针
        res = 0
        l,r = 0, len(height) -1
        while l < r:
            res = max(res, min(height[r] , height[l]) * (r - l))
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return res
