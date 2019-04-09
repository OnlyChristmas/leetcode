'''
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.



Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"


'''



class Solution:
    def toLowerCase(self, str: str) -> str:

        # Approach one   考察ord() ,  chr() ,  以及字符的 ASCII  编码， A~Z：65~90   a~z：97~122
        for i in str:
            if  'A' <= i <= 'Z':
                str = str.replace(i, chr(ord(i)+32))
        return str
