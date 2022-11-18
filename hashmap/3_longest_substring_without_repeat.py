class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            visited = [0] * 256
            for j in range(i, n):
                if visited[ord(s[j])] == True:
                    break
                else:
                    ans = max(ans, j-i+1)
                    visited[ord(s[j])] = True
            visited[ord(s[i])] == False
        return ans
