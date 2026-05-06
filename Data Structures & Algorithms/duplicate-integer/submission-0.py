class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # # Brute force (?) solution
        # # loop up to end
        # for i in range(len(nums)):
        #     # check if nums[i] is member of nums[i::]
        #     if nums[i] in nums[i+1:]:
        #         # break if true
        #         return True
        # return False

        # Hash Set solution kinda similar
        # seen = set()  # Space complexity: n because worst case we have a set of n elements
        # for nums in nums:
        #     if num in seen:
        #         return True
        #     else:
        #         seen.add(num)
        #     return False

        # One-liner but basically same thing
        return len(set(nums)) != len(nums)
        