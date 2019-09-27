'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

'''


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:(x[0],x[1]))
        res = []
        i = 0
        while i < len(intervals):
            j = i +1
            while j < len(intervals) and intervals[i][1] >= intervals[j][0]:
                intervals[i][1] = max(intervals[i][1], intervals[j][1])
                j += 1
            res.append(intervals[i])
            i = j
        return res
