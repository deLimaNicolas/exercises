#Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
#
# 
#
#Example 1:
#
#Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
#Output: [[1,6],[8,10],[15,18]]
#Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
#Example 2:
#
#Input: intervals = [[1,4],[4,5]]
#Output: [[1,5]]
#Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# 
#
#Constraints:
# start and end are both greater than zero
# start must be lower or equal end
# start and end mus† be lower than 104
#
#
#Example 1:
#
#Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
#   [[1,3],[8,10],[2,6],[15,18]]
#Output: [[1,6],[8,10],[15,18]]
#Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
#Example 2:
#
#Input: intervals = [[1,4],[4,5]]
#Output: [[1,5]]
#Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#
# [[1,4],[4,5]]
#
# merge(i, j):
#   newInterval = []
#   newInterval[0] = min(i[0], j[0])
#   newInterval[1] = max(i[1], j[1])
# 
#
# What is considered overlap:
#   se [i0] >= [j0] and [i0] <= [j1]:
#       overlaps
#   se [i1] >= [j0] and [i1] <= [j1]:
#       overlaps
#
#   se overlaps:
#     merge(i, j)
#
# PseudoImplementation:
#
#Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
#       positionsMerged: set()
#       merged_array: []
#       for postion in range(len(intervals)):
#           if position not in positionsMerged: 
#              for positionj in range(len(intervals)):
#                   if isOverlap(intervals[position], intervals[positionj]):
#                       intervals[postition] = unify(intervals[position], intervals[positionj])
#                       postionsMerged.add(positionj)
#               merged_array.ppend(intervals[postition])



#   [[1,3],[8,10],[2,6],[15,18]]
#   [[1,3],[2,6], [8,10], [15,18]]
#
#

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        def isOverlap(interval1: List[int], interval2: List[int]) -> bool:
            return max(interval1[0], interval2[0]) <= min(interval1[1], interval2[1])
        
        def unify(interval1, interval2):
            return [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]

        intervalsLen = len(intervals)

        intervals.sort(key = lambda i : i[0])

        merged = [intervals[0]]
        for px in range(intervalsLen)[1:]:
            print("Comparing ", merged[-1], intervals[px])
            if isOverlap(merged[-1], intervals[px]):
                merged[-1] = unify(merged[-1], intervals[px])
            else:
                merged.append(intervals[px])
        return merged


def main():
    solution = Solution()
    print(solution.merge([[1, 6], [0, 2], [4, 4], [0, 2], [5, 6], [4, 5], [3, 5], [1, 3], [4, 6], [4, 6], [3, 4]]))

main()
