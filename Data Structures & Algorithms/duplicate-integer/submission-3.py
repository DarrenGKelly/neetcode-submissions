from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = Counter(nums)

        if (len(nums) == 0):
            return False

        if (c.most_common(1)[0][1] > 1):
            return True
        
        return False