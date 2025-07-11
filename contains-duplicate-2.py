class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums or len(nums) < 2:
            return False

        present = set()
        present.add(nums[0])
        l, r = 0, 1

        while r < len(nums):
            if not abs(r - l) <= k:
                present.remove(nums[l])
                l += 1
            if nums[r] in present:
                return True
            present.add(nums[r])
            r += 1
            
        return False
