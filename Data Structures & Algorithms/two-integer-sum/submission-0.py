class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stored = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in stored:
                return [stored[diff], i]
            stored[n] = i
            


        