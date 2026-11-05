class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):
        ans = 0

        for num in arr1:
            valid = True

            for other in arr2:
                if abs(num - other) <= d:
                    valid = False
                    break

            if valid:
                ans += 1

        return ans