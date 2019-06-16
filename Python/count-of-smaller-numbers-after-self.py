''''


You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.



'''


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # Approach one 归并排序
        def MergeSort(enum):
            half = len(enum) // 2
            if half:
                left, right = MergeSort(enum[:half]), MergeSort(enum[half:])
                m, n = len(left), len(right)
                i = j = 0
                while i < m or j < n:
                    if j == n or i < m and left[i][1] <= right[j][1]:
                        enum[i+j] = left[i]
                        res[left[i][0]] += j
                        i += 1
                    else:
                        enum[i+j] = right[j]
                        j += 1
            return enum

        if len(nums) < 2: return [0 for _  in range(len(nums))]
        res = [0] * len(nums)
        MergeSort(list(enumerate(nums)))
        return res


        # Approach two
        # 可以构造树状数组  参考 https://www.zybuluo.com/liweiwei1419/note/1391898
