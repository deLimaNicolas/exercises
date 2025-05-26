# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# -1 + 0 = -1 -> 1
# -1 + 1 = 0 -> 0
from typing import List

class Solution:
    def threeSum(self, nums: List[int]):
        result = []
        nums.sort()
        for idx in range(len(nums) - 1):
            left = idx
            right = len(nums) - 1
            cNum = nums[idx]
            if cNum > 0:
                break
            if idx > 0 and cNum == nums[idx - 1]:
                continue
            while left < right:
                lNum = nums[left]
                rNum = nums[right]

                candidate = cNum + lNum + rNum

                if candidate == 0:
                    result.append([cNum, lNum, rNum])
                    left += 1
                    right -=1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                if candidate > 0:
                    right -= 1
                if candidate < 0:
                    left += 1
        return result


def main():
    solution = Solution()
    print(solution.threeSum([-1,0,1,2,-1,-4]))
main()
