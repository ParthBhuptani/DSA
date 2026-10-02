class Solution:
    def generateParenthesis(self, n: int):
        ans = []

        def backtrack(s, open_count, close_count):
            
            # We have used all brackets
            if open_count == n and close_count == n:
                ans.append(s)
                return

            # Add opening bracket
            if open_count < n:
                backtrack(
                    s + '(',
                    open_count + 1,
                    close_count
                )

            # Add closing bracket only if
            # there is an unmatched opening bracket
            if close_count < open_count:
                backtrack(
                    s + ')',
                    open_count,
                    close_count + 1
                )

        backtrack("", 0, 0)

        return ans