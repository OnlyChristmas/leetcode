'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.


'''


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Approach one
        dic = {}
        for i in strs:
            ii = ''.join(sorted(i))
            if dic.get(ii,0) != 0:
                dic[ii].append(i)
            else:
                dic[ii] = [i]
        return [i for i in dic.values()]
