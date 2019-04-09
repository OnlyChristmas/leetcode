'''
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5


'''



class Solution:
    def countSegments(self, s: str) -> int:
        # Approach one    内置函数
        return len(s.split())

        # Approach two     自己实现
#         res = 0
#         flag = False
#         length = len(s)
#         for idx, i in enumerate(s):
#             if i == ' ' and flag :
#                 res += 1
#                 flag = False
#             if i != ' ':
#                 flag = True
#             if length - 1 == idx and i != ' ':
#                 res += 1
#         return res
