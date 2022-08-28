# this can also be done by power set algorithm without recurssion
# there will be 2 types of subsequence of an array
# suppose arr = [3,1,2]
# 1 - contiguous ( [3], [1], [2], [3,1] , [1,2] , [3,1,2] )
# 2 - non contiguous ( [3,2] )

# there can be 2 types of case in making a subsequence
# taking the i th element and not taking the i th element

class Solution:
    def __init__(self):
        self.solve_store = []

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

    # just print all the occurances
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


if __name__ == "__main__":
    x = Solution()
    a = [3, 1, 2]
    # x.solve_print(0, a, [])
    x.solve_return(0, a, [])
    x.solve_store_print()

# LINKS https://www.youtube.com/watch?v=AxNNVECce8c&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=6
