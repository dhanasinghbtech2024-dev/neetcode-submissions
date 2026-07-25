class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            j = target - i
            index_i = nums.index(i)
            if j in nums[index_i + 1:]:
                index_j = nums.index(j, index_i + 1)
                return [index_i, index_j]