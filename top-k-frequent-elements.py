#Given an integer array nums and an integer k, return the k most frequent elements within the array.
#
#The test cases are generated such that the answer is always unique.
#
#You may return the output in any order.
#
#Example 1:
#
#Input: nums = [1,2,2,3,3,3], k = 2
#
#Output: [2,3]
#Example 2:
#
#Input: nums = [7,7], k = 1
#
#Output: [7]
#
#
#Input: nums = [7,7, 8, 8], k = 1
#
#Output: [7]
# 
#
# CONSTRAINTS:
# Input == [] | Output == []
# Array len < 10^4
# -1000 > Array[i] < 1000
# NOTES
#
#
# POSSIBLE SOLUTIONS
#
# Input: nums = [1,2,2,3,3,3], k = 2
# numScore = set()
#  {1: 1, 2: 2, 3: 3}
# 1 -> 2 -> 2 -> 3 -> 3 -> 3 
#  topK
#  for key in numScore:
#     
#
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numScore = {}

        for num in nums:
            if not num in numScore:
                numScore[num] = 0
            numScore[num] += 1   

        numOrderedByFrequency = sorted(numScore.keys(), key=lambda k: numScore[k], reverse=True)
        return numOrderedByFrequency[:k]
def main():
    solution = Solution()
    print(solution.topKFrequent([1,1,1,1,1,1,2,5,5,5,5], k = 2))

main()
