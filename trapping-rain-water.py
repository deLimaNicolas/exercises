from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        heightLen = len(height) - 1

        if heightLen < 2:
            return 0

        left = 0
        right = heightLen
        maxLeft = height[left]
        maxRight = height[right]

        ans = 0

        while left < right:
            if maxLeft < maxRight:
                left += 1
                ans = ans + max((maxLeft - height[left]), 0)
                maxLeft = max(maxLeft, height[left])

            elif maxLeft > maxRight:
                right -= 1
                ans = ans + max((maxRight - height[right]), 0)
                maxRight = max(maxRight, height[right])

            elif maxLeft == maxRight:
                left += 1
                ans = ans + max((maxLeft - height[left]), 0)
                maxLeft = max(maxLeft, height[left])

        return ans

def main():
    solution = Solution()
    print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))

main()
