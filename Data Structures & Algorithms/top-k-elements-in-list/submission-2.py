from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        sorted_keys = sorted(counts, key=counts.get, reverse=True)
        return sorted_keys[:k]
