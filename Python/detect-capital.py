'''
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.

Example 1:
Input: "USA"
Output: True

Example 2:
Input: "FlaG"
Output: False

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
'''

class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """

        # Approach #1
        # Time:  O(1)
        # Space: O(1)
        #
        # if word.lower() == word or word.capitalize() == word or word == word.upper():
            # return True
        # return False

        # Approach #2 直接在return 中判断，进一步简化语句                     注意特殊条件''
        # Time:  O(1)
        # Space: O(1)
        #
        return word.islower() or  word.isupper() or word.istitle() or word == ''
