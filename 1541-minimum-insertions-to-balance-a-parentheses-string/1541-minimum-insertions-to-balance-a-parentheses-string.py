class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0
        need = 0

        for ch in s:
            if ch == '(':
                # Closing parentheses needed must be even
                if need % 2 == 1:
                    ans += 1
                    need -= 1

                # Every '(' requires two ')'
                need += 2

            else:
                need -= 1

                # We have an unmatched ')'
                if need < 0:
                    ans += 1
                    need = 1

        return ans + need