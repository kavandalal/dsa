class Solution:
    def countAndSay(self, n: int) -> str:

        def backtrack(i):
            if i <= 1:
                return '1'

            x = backtrack(i-1)

            ans = ''
            left, right = 0, 0
            count = 0

            while right < len(x):
                if x[right] == x[left]:
                    right += 1
                    count += 1
                else:
                    ans = ans + str(count) + x[left]
                    left = right
                    count = 0
            if count:
                ans = ans + str(count) + x[left]

            return ans

        return backtrack(n)
