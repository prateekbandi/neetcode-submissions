class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        pos = set()
        for num in nums:
            if num in pos:
                return True
            pos.add(num)
        return False