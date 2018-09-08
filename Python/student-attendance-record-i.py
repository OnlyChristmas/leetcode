'''


You are given a string representing an attendance record for a student. The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True

Example 2:
Input: "PPALLL"
Output: False



'''



class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # trick 用or语句反向判断，不用每次都判断两个条件，提升运行效率
        return  False if s.count('A') > 1 or 'LLL'  in s else True
