# M Coloring Decision Problem ( Backtracking , Graph)
# In this problem we have to find the combination of nodes which satisfy conditions
# - no 2 neighbour will have same color
# - only "m" color can be taken into consideration (m == given)

# Adjacency matrix is given and number of colors is given

# Time complexity - n ^ m ( n == nodes , m == colors)


class Solution:
    def solve(self, n, m, adj, colors):
        def is_safe(node, color):
            for it in range(len(adj[node])):
                # if  colors[it] == color:
                if adj[node][it] != 0 and colors[it] == color:
                    return False
                # if color not in adj[node]:
                #     return True
                # return False
            return True

        def backtracking(node):
            if n == node:
                return True
            for j in range(1, m + 1):
                if is_safe(node, j):
                    colors[node] = j
                    if backtracking(node + 1) == True:
                        return True
                    colors[node] = 0
            return False
        return backtracking(0)


if __name__ == '__main__':
    x = Solution()
    colors = [0] * 4
    # result colors list
    adj = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
    # adjacency matrix - where the number of sublist are the nodes - 0 if that node does not have neighbour at that perticula index and 1 if that node contains neighbout
    # suppose x = [[0,1,0], [1,0,1], [0,1,0]]
    # len(x) == 3
    # x[0] == Node A and its neighbour are B as x[0][1] == 1
    # x[1] == Node B and its neighbour are A and C as x[1][0] == 1 and x[1][2] == 1
    # x[2] == Node C and its neighbour are B as x[2][1] == 1
    n = len(colors)
    # n == number of nodes
    m = 3
    # m == number of color that can be taken
    if x.solve(n, m, adj, colors):
        print(colors)
    else:
        print("no combination found")


# LINKS
# https://www.youtube.com/watch?v=052VkKhIaQ4
# https://www.geeksforgeeks.org/m-coloring-problem-backtracking-5/
# https://www.youtube.com/watch?v=wuVwUK25Rfc&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=16
