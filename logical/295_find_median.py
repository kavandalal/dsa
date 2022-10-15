# Min heap and Max heap is used for implementation
# LINKS https://www.youtube.com/watch?v=itmhHWaHupI


import heapq


class MedianFinder:

    def __init__(self):
        self.small = []  # going to implement max heap
        self.large = []  # going to implement min heap
        # by default in python there is only min heap, to implement max heap we have to multiply every value that is to be inserted in max heap with -1 to get correct max heap

    def addNum(self, num: int) -> None:
        # by deafult add every number to the small (maxheap)
        heapq.heappush(self.small, -1 * num)  # as this is maxheap (*-1)

        # check the max value of small and min value of large
        if self.small and self.large and not (-1 * self.small[0] <= self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # uneven size (small > large)
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # uneven size (small < large)
        if len(self.small) + 1 < len(self.large):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # more element in small
        if len(self.small) > len(self.large):
            return -1 * self.small[0]

        # more element in large
        if len(self.small) < len(self.large):
            return self.large[0]

        # equal element in small and large
        return ((-1 * self.small[0]) + self.large[0]) / 2
