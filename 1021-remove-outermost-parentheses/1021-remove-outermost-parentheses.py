class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        depth = 0

        for ch in s:
            if ch == '(':
                depth += 1
                # Don't add outermost '('
                if depth > 1:
                    ans.append(ch)
            else:
                depth -= 1

                # Don't add outermost ')'
                if depth > 0:
                    ans.append(ch)

        return ''.join(ans)