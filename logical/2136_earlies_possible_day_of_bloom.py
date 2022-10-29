# LINKS https://www.youtube.com/watch?v=R6Mc2W6rOZw

class Solution:
    def earliestFullBloom(self, plantTime: list[int], growTime: list[int]) -> int:
        n = len(plantTime)
        l = [(plantTime[k], growTime[k]) for k in range(n)]
        l.sort(key=lambda x: x[1], reverse=True)
        print(l)
        start = 0
        ans = 0
        for i in range(n):
            start += l[i][0]
            ans = max(ans, start + l[i][1])

        return ans
