class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            find = target - n
            if find in seen:
                return [seen[find], i]
            if n not in seen:
                seen.update({n : i})