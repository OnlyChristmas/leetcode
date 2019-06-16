''''
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.


'''

class compare(str):
    def __lt__(x, y):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not nums:return ""
        nums = sorted(list(map(str, nums)), key=compare)
        return '0' if nums[0]=='0' else "".join(nums)   #  当有多个零时候，只保留一个。单独的零补在末尾
