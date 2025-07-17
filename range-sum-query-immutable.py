class NumArray:

    def __init__(self, nums: List[int]):
        self.values = []
        for idx in range(len(nums)):
            if idx > 0:
                self.values.append(nums[idx] + self.values[idx - 1])
            else:
                self.values.append(nums[idx])
        
        print(self.values)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.values[right]
        else:
            return self.values[right] - self.values[left - 1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
