
'''
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
Credits:
Special thanks to @ syedee for adding this problem and creating all test cases

'''


```
class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # 一次遍历
        # return [bin(i)[2:].count('1') for i in range(num+1)]



        # method two   更加高效的解法，少调用内置函数，挖掘数据中的规律


#    0000    0
# -------------
#    0001    1
# -------------
#    0010    1
#    0011    2
# -------------
#    0100    1
#    0101    2
#    0110    2
#    0111    3
# -------------
#    1000    1
#    1001    2
#    1010    2
#    1011    3
#    1100    2
#    1101    3
#    1110    3
#    1111    4

        # ans = [0]
        # while len(ans) < num + 1:
        #     ans += [1 + x for x in ans]
        # return ans[:num+1]


      # Approach #3   利用 i & i-1 进一步挖掘比特位计数的规律。  每个数i所对应的比特位计数的答案是 i & i-1 计算结果的数字，所对应的比特位计数结果加一。


#    bin    '1'  i&(i-1)
#    0000    0
# -----------------------
#    0001    1    0000
# -----------------------
#    0010    1    0000
#    0011    2    0010
# -----------------------
#    0100    1    0000
#    0101    2    0100
#    0110    2    0100
#    0111    3    0110
# -----------------------
#    1000    1    0000
#    1001    2    1000
#   1010    2    1000
#   1011    3    1010
#   1100    2    1000
#   1101    3    1100
#   1110    3    1100
#   1111    4    1110

        res = [0]
        for i in range(1,num+1):
            res += [res[ i & i-1] + 1]
        return res






```
