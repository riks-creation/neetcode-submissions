class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        included = set()
        for n in nums:
            if n in included:
                return True
            included.add(n)
        return False
        