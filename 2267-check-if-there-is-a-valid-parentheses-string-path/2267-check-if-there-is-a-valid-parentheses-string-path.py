from functools import cache

class Solution:
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        # Total number of characters in any path
        length = m + n - 1

        # A valid parentheses string must have even length
        if length % 2 == 1:
            return False

        # First character must be '('
        if grid[0][0] == ')':
            return False

        @cache
        def dfs(r, c, balance):

            # Invalid balance
            if balance < 0:
                return False

            # Not enough cells left to close all open brackets
            remaining = (m - 1 - r) + (n - 1 - c)

            if balance > remaining:
                return False

            # Reached bottom-right
            if r == m - 1 and c == n - 1:
                return balance == 0

            # Try moving down
            if r + 1 < m:
                next_balance = balance

                if grid[r + 1][c] == '(':
                    next_balance += 1
                else:
                    next_balance -= 1

                if dfs(r + 1, c, next_balance):
                    return True

            # Try moving right
            if c + 1 < n:
                next_balance = balance

                if grid[r][c + 1] == '(':
                    next_balance += 1
                else:
                    next_balance -= 1

                if dfs(r, c + 1, next_balance):
                    return True

            return False

        return dfs(0, 0, 1)