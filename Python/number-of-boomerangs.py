'''
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]



'''



class Solution:

    # Approach one
#     def recursion(self,n): #'定义递归函数实现求阶乘功能'
#         if n==1:
#             return 1
#         else:
#             return  n * self.recursion(n-1)

#     def numberOfBoomerangs(self, points: List[List[int]]) -> int:
#         res = 0
#         for i, n in enumerate(points):
#             dic = {}
#             for j, m in enumerate(points):
#                 ans = abs(m[0] - n[0])**2 + abs(m[1] - n[1])**2
#                 dic[ans] = dic.get(ans,0) + 1
#             for v in dic.values():
#                 if v > 1:
#                     if v >= 4:
#                         res += self.recursion(v)//2
#                     else:
#                         res += self.recursion(v)
#         return res




    # Approach two
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        from collections import Counter
        fouc = lambda x, y : x**2 + y**2
        for n in points:
            for v in Counter([ fouc(m[0] - n[0] , m[1] - n[1])  for m in points]).values():
                res += v * (v-1)
        return res
