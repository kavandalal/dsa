# this can also be done by power set algorithm without recurssion
# there will be 2 types of subsequence of an array
# suppose arr = [3,1,2]
# 1 - contiguous ( [3], [1], [2], [3,1] , [1,2] , [3,1,2] )
# 2 - non contiguous ( [3,2] )

# there can be 2 types of case in making a subsequence
# taking the i th element and not taking the i th element

# time complexity - 2 ^ n
# n being number of elements
# 2 because there will always be 2 possibility, taking the eleemnt or not taking the element


class Solution:
    def __init__(self):
        self.solve_store = []

    # just print all the occurances
    def solve_store_print(self):
        # sorting by keeping thr length of the list into consideration
        self.solve_store.sort(key=len)
        print(self.solve_store)
        return

    # to store all the occurance in the variable of the class
    def solve_return(self, i, arr, ansArr=[]):
        if i >= len(arr):
            newElem = ansArr.copy()
            self.solve_store.append(newElem)
            return
        # print(type(ansArr), i)
        ansArr.append(arr[i])
        # taking the i th element in the answer Arr
        self.solve_return(i + 1, arr, ansArr)
        ansArr.pop()
        # not taking the element in the answer Arr
        self.solve_return(i + 1, arr, ansArr)

    # print all the subsequence, no need to store it
    def solve_print(self, i, arr, ansArr=[]):
        if i >= len(arr):
            print(ansArr)
            return
        # print(type(ansArr), i)
        ansArr.append(arr[i])
        # taking the i th element in the answer Arr
        self.solve_print(i + 1, arr, ansArr)
        ansArr.pop()
        # not taking the element in the answer Arr
        self.solve_print(i + 1, arr, ansArr)

    # find all the subsequence which has desired sum
    def find_subseq_sum(self, i, arr, total, ansArr=[]):
        # print('+', ansArr)
        if i >= len(arr):
            if sum(ansArr) == total:
                print(ansArr)
        if i < len(arr):
            ansArr.append(arr[i])
            self.find_subseq_sum(i + 1, arr,  total, ansArr)
            ansArr.pop()
            self.find_subseq_sum(i + 1, arr,  total, ansArr)

    # find only the first summation subsequence and then stop
    def find_subseq_sum_only_1(self, i, arr, total, ansArr=[]):
        if i >= len(arr):
            if sum(ansArr) == total:
                print(ansArr)
                return True
            else:
                return False
        if i < len(arr):
            ansArr.append(arr[i])
            if self.find_subseq_sum_only_1(i + 1, arr,  total, ansArr):
                return True
            ansArr.pop()
            if self.find_subseq_sum_only_1(i + 1, arr,  total, ansArr):
                return True
            return False

    # return the count of total subsequence with the given sum
    def find_subseq_sum_count(self, i, arr, total, ansArr=[]):
        # print('+', ansArr)
        if i >= len(arr):
            if sum(ansArr) == total:
                return 1
            else:
                return 0
        if i < len(arr):
            ansArr.append(arr[i])
            l = self.find_subseq_sum_count(i + 1, arr,  total, ansArr)
            ansArr.pop()
            r = self.find_subseq_sum_count(i + 1, arr,  total, ansArr)
            return l + r


if __name__ == "__main__":
    x = Solution()
    # a = [3, 1, 2]
    a = [1, 2, 1]
    # x.solve_print(0, a, [])
    # x.solve_return(0, a, [])
    # x.solve_store_print()
    # x.find_subseq_sum(0, a, 2, [])
    # x.find_subseq_sum_only_1(0, a, 2, [])
    # print(x.find_subseq_sum_count(0, a, 2, []))

# LINKS
# https://www.youtube.com/watch?v=AxNNVECce8c&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=6
# https://www.youtube.com/watch?v=eQCS_v3bw0Q&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=7
