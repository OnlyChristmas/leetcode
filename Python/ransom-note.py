'''

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true


'''


class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # method one 用内置函数做出字典影响效率
        # dic1 , dic2 = collections.Counter(ransomNote) , collections.Counter(magazine)
        # for key1 , value1 in dic1.items():
        #     value2 = dic2.get(key1)
        #     if value2 == None or value2 < value1:
        #         return False
        # return True



        # method two  代码简洁，但是有冗余操作
        # return all([ransomNote.count(i) <= magazine.count(i)  for i in  set(ransomNote)])


        # method three   只需要一次遍历，高效
        for i in ransomNote:
            if i in magazine:
                magazine = magazine.replace(i,'',1)
            else:
                return False
        return True


        # Approach #4 字典操作，代码简洁，但并不高效。
        # return not collections.Counter(ransomNote) - collections.Counter(magazine)
