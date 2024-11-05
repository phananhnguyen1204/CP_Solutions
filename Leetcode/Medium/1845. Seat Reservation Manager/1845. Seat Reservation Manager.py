from heapq import heappush, heappop
class SeatManager:

    def __init__(self, n: int):
        self.unreserve_seats = [i for i in range(1, n + 1)]

    def reserve(self) -> int:
        return heappop(self.unreserve_seats)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.unreserve_seats, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)