class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                slow = nums[0]
                while slow != fast:
                    slow = nums[slow]
                    fast = nums[fast]
                return slow

