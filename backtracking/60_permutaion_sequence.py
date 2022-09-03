# 60 LEETCODE - Permutation sequence
# find the kth permutaion of the list having n number i.e. [1,2,3,...,n]

class Solution:
    def solve(self, n, k):
        fact = 1
        num = []
        for i in range(1, n):
            fact *= i
            num.append(i)
        num.append(n)
        ans = ''
        k = k - 1
        while True:
            x = num[k // fact]
            ans = ans + str(x)
            num.remove(x)
            if not num:
                break
            k = k % fact
            fact = fact // len(num)
        return ans


if __name__ == '__main__':
    x = Solution()
    n = 4
    k = 9
    print(x.solve(n, k))


# LINKS
# https://www.youtube.com/watch?v=wT7gcXLYoao
