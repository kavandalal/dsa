# 131 LEETCODE - Palindrome partition

class Solution:
    def solve(self, s):
        res = []
        path = []

        def is_palindrome(subs):
            size = len(subs)
            for i in range(size // 2):
                if subs[i] != subs[size - i - 1]:
                    return False
            return True

        def backtracking(index, path, res):
            if index == len(s):
                res.append(path[:])
                return
            for i in range(index, len(s)):
                if is_palindrome(s[index: i + 1]):
                    path.append(s[index: i + 1])
                    backtracking(i + 1, path, res)
                    path.pop()

        backtracking(0, path, res)
        return res


if __name__ == '__main__':
    x = Solution()
    c = 'aabb'
    print(x.solve(c))


# LINKS
# https://www.youtube.com/watch?v=WBgsABoClE0&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=17
