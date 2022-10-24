class Solution:
    def maxLength(self, arr: list[str]) -> int:

        def uniqueChar(s):
            if len(s) != len(set(s)):
                return 0
            return len(s)

        def backtrack(n, currentStr, maxi):
            if n == 0 and uniqueChar(currentStr) > maxi:
                maxi = len(currentStr)
                print(currentStr, n)
                return maxi
            if n == 0:
                return 0

            pick = backtrack(n-1, currentStr + arr[n-1], maxi)
            notpick = backtrack(n-1, currentStr, maxi)

            return max(pick, notpick)

        maxi = 0
        if len(arr) == 1:
            return uniqueChar(arr[0])

        maxi = backtrack(len(arr), '', maxi)
        return maxi
