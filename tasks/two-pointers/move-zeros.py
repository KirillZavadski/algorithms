class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        second_i = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[second_i] = nums[second_i], nums[i]
                second_i += 1