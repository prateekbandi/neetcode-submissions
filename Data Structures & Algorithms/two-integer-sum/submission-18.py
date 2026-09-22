class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for index, num in enumerate(nums):
            difference = target - num
            if difference in dict1:
                return [dict1[difference], index]
            dict1[num] = index
        