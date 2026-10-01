class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:

            # Opening bracket
            if ch in '([{':
                stack.append(ch)

            # Closing bracket
            else:
                # No opening bracket to match
                if not stack:
                    return False

                # Wrong type of opening bracket
                if stack[-1] != pairs[ch]:
                    return False

                # Correct match
                stack.pop()

        # All brackets must be matched
        return len(stack) == 0