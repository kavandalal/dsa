import math


class Solution:
    def countBits(self, n: int) -> list[int]:
        if n == 0:
            return [0]
        result = [0, 1]
        base2 = math.log(2)
        for i in range(2, n+1):
            j = math.log(i) / base2
            k = 2**int(j)
            if k == i:
                result.append(1)
            else:
                result.append(1 + result[i - k])

        return result
