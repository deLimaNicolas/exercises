#You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
#Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
#
# 
#
#Example 1:
#
#Input: nums = [2,3,2]
#Output: 3
#Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
#Example 2:
#
#Input: nums = [1,2,3,1]
#               
#Output: 4
#Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#Total amount you can rob = 1 + 3 = 4.
#Example 3:
#
#Input: nums = [1,2,3]
#Output: 3

from typing import List

class Solution:
    def rob(self, nums: List[int]):
        def rob_logic(nums):
            lastest_high_value = [nums[0]]
            lastest_high_value.append(max(nums[0], nums[1]))

            print(lastest_high_value)

            for num_index in range(2, num_len - 1):
                rob_current_value = nums[num_index] + lastest_high_value[num_index -2]
                do_not_rob = lastest_high_value[num_index -1]

                max_decision = max(rob_current_value, do_not_rob)
                lastest_high_value.append(max_decision)

            return lastest_high_value.pop()

        num_len = len(nums)
        if num_len == 1:
            return nums[0]

        if num_len == 2:
            return max(nums[0], nums[1])

        return max(rob_logic(nums[1:]), rob_logic(nums[0:-1]))

def main():
    solution = Solution()
    print(solution.rob([1,3,1,3,100]))


main()
