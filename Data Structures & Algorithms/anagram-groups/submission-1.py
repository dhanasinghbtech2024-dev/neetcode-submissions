from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            sorted_str = tuple(sorted(s))
            ans[sorted_str].append(s)
        return list(ans.values())