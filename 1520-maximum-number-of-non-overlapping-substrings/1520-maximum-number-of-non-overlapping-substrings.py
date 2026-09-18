class Solution:
    def maxNumOfSubstrings(self, s: str):
        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        # Find first and last occurrence
        for i, ch in enumerate(s):
            x = ord(ch) - ord('a')
            first[x] = min(first[x], i)
            last[x] = i

        intervals = []

        # Build the smallest valid interval for each character
        for x in range(26):
            if first[x] == n:
                continue

            l = first[x]
            r = last[x]
            i = l
            valid = True

            while i <= r:
                y = ord(s[i]) - ord('a')

                # This character appeared before l,
                # so this interval cannot be valid.
                if first[y] < l:
                    valid = False
                    break

                # We need to include all occurrences of this character.
                r = max(r, last[y])
                i += 1

            if valid:
                intervals.append((l, r))

        # Select maximum number of non-overlapping intervals
        intervals.sort(key=lambda x: x[1])

        ans = []
        end = -1

        for l, r in intervals:
            if l > end:
                ans.append(s[l:r + 1])
                end = r

        return ans