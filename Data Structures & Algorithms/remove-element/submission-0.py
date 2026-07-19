class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 1. Calculate how many valid elements will remain
        lis = len(nums) - nums.count(val)
        nums.sort(key=lambda x: x == val)
        return lis
