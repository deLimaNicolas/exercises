from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numLen = len(numbers)
        left = 0
        right =  numLen - 1

        if not numbers:
            return []

        while right >= 0 and left < numLen:
            if numbers[left] + numbers[right] == target:
                if numbers[left] != numbers[right]:
                    return[left + 1, right + 1]
                else:
                    right -= 1
                    left += 1


            if numbers[left] + numbers[right] > target:
                right -= 1
                continue

            if numbers[left] + numbers[right] < target:
                left += 1
                continue



def main():
    solution = Solution()
    print(solution.twoSum(numbers = [1,2,3,4], target = 3))

main()

