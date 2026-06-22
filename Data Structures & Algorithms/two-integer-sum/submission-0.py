class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for index, val in enumerate(nums):
            complement = target - val
            if complement in dict1:
                return [dict1[complement], index]
            dict1[val] = index
