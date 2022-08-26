class Solution:
    def print_i_n(self, i, n):
        if i > n:
            return
        print(i)
        self.print_i_n(i + 1, n)

    def print_i_n_backtr(self, i, n):
        if i < 0:
            return
        self.print_i_n_backtr(i - 1, n)
        print(i)


if __name__ == '__main__':
    x = Solution()
    # x.print_i_n(0, 5)
    # x.print_i_n_backtr(5, 5)
