#You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#
#Find two lines that together with the x-axis form a container, such that the container contains the most water.
#
#Return the maximum amount of water a container can store.
#
#Notice that you may not slant the container.
#
#
#Input: height = [1,8,6,2,5,4,8,3,7]
#Output: 49
#Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
#Example 2:
#
#Input: height = [1,1]
#Output: 1
#
#                 2 * 1 -> (ith  - jth) * min(height[ith], height[th]) 
#Input: height = [1,1,2]
#Output: 1
#                [1, 2, 3, 4]
#                 |  |  |  
#                  4  |  3 
#                     6
#               [1, 10, 5, 10, 2, 4]
                 #6  20  16  12 4  4
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left

            h = min(height[left], height[right])
            current_area = width * h
            max_area = max(max_area, current_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
