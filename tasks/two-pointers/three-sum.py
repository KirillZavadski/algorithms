class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets = []
        nums.sort()
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                continue
            if nums[i] + nums[len(nums) - 2] + nums[len(nums) - 1] < 0:
                continue

            y = i + 1
            z = len(nums) - 1
            while y < z:
                if nums[i] + nums[y] + nums[z] > 0:
                    z -= 1
                elif nums[i] + nums[y] + nums[z] < 0:
                    y += 1
                else:
                    triplets.append([nums[i], nums[y], nums[z]])
                    y, z = y + 1, z - 1
                    while y < z and nums[y] == nums[y - 1]:
                        y += 1
                    while y < z and nums[z] == nums[z + 1]:
                        z -= 1
        return triplets