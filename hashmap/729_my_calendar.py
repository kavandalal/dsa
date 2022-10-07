from sortedcontainers import SortedDict


class MyCalendar:
    def __init__(self):
        self.calendar = SortedDict({float('inf'): float('inf')})
        # self.calendar = SortedDict({float('-inf'): float('-inf')})

    def book(self, start: int, end: int) -> bool:
        ix = self.calendar.bisect_right(start)
        print(start, self.calendar.peekitem(ix))
        k, v = self.calendar.peekitem(ix)
        res = end <= v
        if res:
            self.calendar[end] = start
        return res



# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
x = [[10, 20], [40, 50], [5, 15], [20, 30], [45, 60]]
for i in x:
    print(obj.book(i[0], i[1]))
