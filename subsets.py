from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset[:])
                print(f"{subset[:]} appended")
                return 
            print("Don't pick Num ", nums[i])
            dfs(i + 1)

            print("Pick Num ", nums[i])
            subset.append(nums[i])
            dfs(i + 1)

            # Undo num pick
            subset.pop()
        dfs(0)
        return res
