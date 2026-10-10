class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        # If we can reduce every difference to zero
        if sum(diffs) <= k:
            return 0

        # Binary search for the smallest achievable maximum difference
        left, right = 0, max(diffs)

        while left < right:
            mid = (left + right) // 2

            operations = sum(max(0, d - mid) for d in diffs)

            if operations <= k:
                right = mid
            else:
                left = mid + 1

        limit = left

        # Reduce every difference to at most limit
        used = sum(max(0, d - limit) for d in diffs)
        remaining = k - used

        # Calculate the squared sum after leveling
        ans = sum(min(d, limit) ** 2 for d in diffs)

        # Each remaining operation changes limit -> limit - 1
        ans -= remaining * (2 * limit - 1)

        return ans