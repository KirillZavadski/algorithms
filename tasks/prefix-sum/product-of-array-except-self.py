class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1] * len(nums)
        suf = [1] * len(nums)
        new_arr = []

        for i in range(1, len(nums)):
            pref[i] = pref[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i + 1]

        for i in range(len(nums)):
            new_arr.append(pref[i] * suf[i])
        
        return new_arr