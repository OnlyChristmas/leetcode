'''
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o
+------------->
0  1  2  3  4
Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6


'''


# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    def maxPoints(self, points: List[Point]) -> int:

        # Approach one
        # 测试例子  [[0,0],[94911151,94911150],[94911152,94911151]]  由于数字较为接近，斜率会近似相等。 用 Decimal 提高精度

        from decimal import Decimal
        res = 0
        for i, n in enumerate(points):
            slopes = {}
            same = 0
            for j in range(i+1, len(points)):
                if n.x == points[j].x and n.y == points[j].y:
                    same += 1
                    continue
                slope = float('inf') if n.x == points[j].x else Decimal(n.y - points[j].y) / (n.x - points[j].x)
                slopes[slope] = slopes.get(slope, 1) + 1
            max_slope_num = max(slopes.values()) if slopes != {} else 1
            res =  res if max_slope_num == 0  else   max(( max_slope_num + same),res)
        return res
