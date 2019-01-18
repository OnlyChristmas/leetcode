'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 栈数据结构
        dic = {'(':')','{':'}','[':']'}
        answer = ['k']
        for i in s:
            if dic.get(answer[-1]) != i:
                answer.append(i)
            else:
                del answer[-1]
        if answer == ['k']: return True
        return False
