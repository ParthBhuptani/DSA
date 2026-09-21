class Solution:
    def resultArray(self, nums, k):
        dp = [0] * k
        ans = [0] * k

        for num in nums:
            new_dp = [0] * k

            # Start a new subarray
            remainder = num % k
            new_dp[remainder] += 1

            # Extend previous subarrays
            for r in range(k):
                if dp[r]:
                    new_remainder = (r * num) % k
                    new_dp[new_remainder] += dp[r]

            dp = new_dp

            # Add all subarrays ending here
            for r in range(k):
                ans[r] += dp[r]

        return ans