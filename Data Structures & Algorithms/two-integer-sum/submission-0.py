class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_index = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in value_index:
                return [value_index[diff], i]
            value_index[n] = i
        return