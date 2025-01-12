class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix = [0] * (n + 1)
        for start, end, seat in bookings:
            prefix[start] += seat
            if end < n:
                prefix[end + 1] -= seat

        res = []
        for flight in range(1, n + 1):
            prefix[flight] += prefix[flight - 1]
            res.append(prefix[flight])

        return res