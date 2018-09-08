'''
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''



class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 思路一:  简单的遍历除以小于他的数,效率太低了!
        # 思路二:　遍历除以小于他一半的数，有率提升一倍
        # 思路三:  动态简历素数表,这样居然还不行?!效率还是低
        # num = 0
        # result = [2  ]
        # for i in range(2, n):
        #     for j in range(len(result)):
        #         if i % result[j] == 0 and i!=result[j]:
        #             break
        #         if j==len(result)-1:
        #             result.append(i)
        #             num += 1
        # return num

        # 思路四: Sieve of Eratosthenes(埃拉托色尼筛法，简称埃氏筛法)，参考维基百科：https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
        # fasle 表示不是素数, true 代表素数. 所以总和是多少,最后就有多少个.


        # 注意审题边界条件,是小于n,不包括n
        if n < 2:
            return 0     # 注意 数组越界的情况

        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5)+1):    # 在选择除数时候的一个小技巧.大于一半的数是不可能做除数的. 事实证明, 能够节省400ms的时间
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])  # 非常简洁的语句, 从小到大用埃氏筛法, 将每一个不是素数的数筛选掉.大大减少出发的数量.
        return sum(primes)
