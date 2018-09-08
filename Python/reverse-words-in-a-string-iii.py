'''
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.

''''



class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # method one  利用字符串的反序以及分离拼接，一行搞定
        # return   ' '.join([x[::-1]  for x in s.split(' ')])


        # method two  可以先对字符串反序，再对列表元素反序。进一步简化代码
        return ' '.join(s[::-1].split()[::-1])
