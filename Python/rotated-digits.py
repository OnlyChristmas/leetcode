'''

X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation:
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
Note:

N  will be in range [1, 10000].

'''



class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        # Approach #1
        # res = 0
        # ban_num = set(['3','4','7'])
        # agree_num = set(['2','5','6','9'])
        # for num in range(N+1):
        #     lookup = set(list(str(num)))
        #     if lookup & ban_num:
        #         continue
        #     if lookup & agree_num:
        #         res += 1
        # return res

        # Appproach #2
        res = 0
        for num in range(N+1):
            s_num =  str(num)
            if '3' not in s_num and '4' not in s_num and  '7' not in s_num:
                if '2' in s_num or '5' in s_num or '6' in s_num or '9' in s_num:
                    res += 1
        return res


            
