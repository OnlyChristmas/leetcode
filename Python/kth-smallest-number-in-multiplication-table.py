class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # 寻找乘法表中第k大的数。


        # 暴力破解法  需要空间复杂度O(m*n) 时间复杂度O(m*n*(log(m*n)+1))
        # 二分法  空间复杂度O(1) 时间复杂度O(min(m,n)*log(m*n))


        if m == 1 or n == 1: return k
        l, r = 1, m * n
        if m > n:
            n, m = m, n
        while l < r:
            mid = l + (r - l) // 2
            count = 0
            for i in range(1, m + 1):
                count += min(mid // i, n)
            if count < k:
                l = mid + 1
            else:
                r = mid
        return l
