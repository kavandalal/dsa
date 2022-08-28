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

    def palindrome_rec(self, arr, i, n):
        if i >= n // 2:
            return True
        if arr[i] != arr[n - i - 1]:
            return False
        return self.palindrome_rec(arr, i + 1, n)

    def swap_rec(self, arr, i, n):
        if i >= n // 2:
            return
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
        self.swap_rec(arr, i + 1, n)

    def fibonnaci_rec(self, n):
        if n <= 1:
            return n
        return self.fibonnaci_rec(n - 1) + self.fibonnaci_rec(n - 2)


if __name__ == '__main__':
    X = Solution()
    # X.print_i_n(0, 5)
    # X.print_i_n_backtr(5, 5)
    # y1 = [1,1,2,2,3,2,2,1,1]
    # z1 = len(y1)
    # print(X.palindrome_rec(y1 ))
    # y2 = [2, 4, 6, 8, 0, 3, 6]
    # z2 = len(y2)
    # print(X.swap_rec(y2, 0, z2))
    print(X.fibonnaci_rec(4))
