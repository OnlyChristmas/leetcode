'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
'''



class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # First method 遍历方法
        # new_numbers = sorted(set(numbers))
        # for i in range(len(new_numbers)):
        #     for j in range(i,len(new_numbers)):
        #         if new_numbers[i] + new_numbers[j] == target:
        #             index1 = numbers.index(new_numbers[i])+1
        #             numbers.remove(new_numbers[i])
        #             return [index1, numbers.index(new_numbers[j])+2]



        # Second method
        # new_numbers = sorted(set(numbers))
        # for i in range(len(new_numbers)):
        #     number2 = target- new_numbers[i]
        #     if number2 in new_numbers:
        #         if number2 == new_numbers[i]:
        #             return [numbers.index(new_numbers[i])+1, numbers.index(number2)+2]   # 处理number1 == number2 相同的情况，他们总是挨着
        #         return [numbers.index(new_numbers[i])+1, numbers.index(number2)+1]


        # third method
        # new_numbers = sorted(set(numbers))
        # for i in range(len(new_numbers)):
        #     number2 = target- new_numbers[i]
        #     if number2 in new_numbers:
        #         ans = numbers.index(new_numbers[i])+1
        #         numbers.remove(new_numbers[i])
        #         return [ans, numbers.index(number2)+2]


        # fourth method  利用字典，巧妙地去掉了重复元素，并且不用特殊处理两个因子相等的情况。
        # check={}
        # for i in range(len(numbers)):
        #     if numbers[i] in check:
        #         return [check.get(numbers[i])+1,i+1]
        #     else:
        #         check[target-numbers[i]]=i

        # fifth method
        dic = {}
        for i,n in enumerate(numbers):
            s = target - n
            if s not in dic:    # 巧妙避免两个相同元素的情况
                dic[n] = i
            else:
                return [dic[s] +1 , i+1]
