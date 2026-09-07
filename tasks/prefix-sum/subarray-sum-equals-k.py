class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_counts = {0: 1}
        current_sum = 0
        count = 0
        for n in nums:
            current_sum += n

            needed = current_sum - k
            if needed in prefix_counts:
                count += prefix_counts[needed]

            if current_sum in prefix_counts:
                prefix_counts[current_sum] += 1
            else:
                prefix_counts[current_sum] = 1
        return count