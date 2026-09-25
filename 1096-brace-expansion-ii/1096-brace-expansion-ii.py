class Solution:
    def braceExpansionII(self, expression: str):
        def parse(i):
            result = set()
            current = {""}

            while i < len(expression) and expression[i] != '}':
                
                if expression[i] == '{':
                    sub_result, i = parse(i + 1)

                elif expression[i] == ',':
                    result |= current
                    current = {""}
                    i += 1
                    continue

                else:
                    sub_result = {expression[i]}
                    i += 1

                # Concatenate current results with sub_result
                current = {
                    a + b
                    for a in current
                    for b in sub_result
                }

            result |= current

            # Skip '}'
            if i < len(expression) and expression[i] == '}':
                i += 1

            return result, i

        result, _ = parse(0)

        return sorted(result)