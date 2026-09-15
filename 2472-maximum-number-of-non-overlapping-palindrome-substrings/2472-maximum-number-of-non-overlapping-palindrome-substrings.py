class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # dp[i] = maximum number of palindromes
        # we can choose from s[0:i]
        dp = [0] * (n + 1)

        # Check every possible palindrome by expanding
        # around its center
        for i in range(n):
            
            # Odd-length palindrome
            left = right = i

            while left >= 0 and right < n and s[left] == s[right]:
                length = right - left + 1

                if length >= k:
                    dp[right + 1] = max(
                        dp[right + 1],
                        dp[left] + 1
                    )

                left -= 1
                right += 1

            # Even-length palindrome
            left = i
            right = i + 1

            while left >= 0 and right < n and s[left] == s[right]:
                length = right - left + 1

                if length >= k:
                    dp[right + 1] = max(
                        dp[right + 1],
                        dp[left] + 1
                    )

                left -= 1
                right += 1

            # We can always skip s[i]
            dp[i + 1] = max(dp[i + 1], dp[i])

        return dp[n]