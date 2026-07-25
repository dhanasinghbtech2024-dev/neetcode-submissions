class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nu = set(nums)
        if len(nu) == len(nums):
            return False
        else:
            return True