class MyCalendarTwo:

    def __init__(self):
        self.events = []
        self.overlap = []

    def book(self, startTime: int, endTime: int) -> bool:
        for s, e in self.overlap:
            if s < endTime and startTime < e:
                return False
        
        for s, e in self.events:
            if s < endTime and startTime < e:
                self.overlap.append([max(s, startTime), min(e, endTime)])
        
        self.events.append([startTime, endTime])
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)