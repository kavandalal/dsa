class MyCalendarTwo:

    def __init__(self):
        self.overlaps = []
        self.store = []

    def book(self, start: int, end: int) -> bool:
        for i, j in self.overlaps:
            if start < j and end > i:
                return False
            """
            this condition is kept after thinking alot 
            there can be 3 case take into consideration 
            1) 1st comes [5,15] then comes [10,20]
            2) 1st comes [10,20] then comes [5,15]
            3) 1st comes [5,20] then comes [10,15]
            we have to not use, this is an overlapping condition, all 3 types
            so to solve this we can see that start(new) < j(old) and end(new) > j(old)
            """

        for i, j in self.store:
            if i < end and j > start:
                self.overlaps.append((max(i, start), min(j, end)))
        self.store.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
