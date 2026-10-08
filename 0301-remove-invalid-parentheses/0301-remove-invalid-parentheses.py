class Solution:
    def removeInvalidParentheses(self, s: str):
        def isValid(string):
            balance = 0

            for ch in string:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        result = []
        queue = {s}
        found = False

        while queue and not found:

            next_level = set()

            for string in queue:

                if isValid(string):
                    result.append(string)
                    found = True

            # If we already found valid strings,
            # don't remove anything further.
            if found:
                break

            for string in queue:

                for i in range(len(string)):
                    # Only remove parentheses
                    if string[i] not in "()":
                        continue

                    new_string = string[:i] + string[i + 1:]
                    next_level.add(new_string)

            queue = next_level

        return result