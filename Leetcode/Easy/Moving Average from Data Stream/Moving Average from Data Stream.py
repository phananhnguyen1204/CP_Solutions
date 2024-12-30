class MovingAverage:

    def __init__(self, size: int):
        self.q = deque()
        self.size = size
        self.sum = 0

    def next(self, val: int) -> float:
        self.q.append(val)
        self.sum += val
        res = self.sum / min(self.size, len(self.q))

        if len(self.q) >= self.size:
            self.sum -= self.q.popleft()
        return res
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)