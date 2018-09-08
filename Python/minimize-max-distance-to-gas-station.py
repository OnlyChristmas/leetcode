'''
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"

Note:
letters has a length in range [2, 10000].
letters consists of lowercase letters, and contains at least 2 unique letters.
target is a lowercase letter.


'''




class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        # method one   ord()，chr（）函数 ， 没有充分利用letters有序这个条件
        # ascii_target = ord(target)
        # while ascii_target:
        #     ascii_target += 1
        #     if ascii_target > 122:
        #         ascii_target -= 26
        #     if chr(ascii_target) in letters:
        #         return chr(ascii_target)


        # method two 直接比较字符大小(letters有序)
        # for letter in letters:
        #     if letter > target:
        #         return letter
        # return letters[0]

        # Approach #3  Binary Search
        if target >= letters[-1]: return letters[0]
        l , r = 0 , len(letters)-1
        while l < r:
            mid = (r + l) // 2
            if letters[mid] > target:
                r = mid
            else:
                l = mid + 1
        return letters[l]
