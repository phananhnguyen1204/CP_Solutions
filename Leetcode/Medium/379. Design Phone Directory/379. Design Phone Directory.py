class PhoneDirectory:
    # 0 <= number < maxNumbers
    # keep track of unassigend number
    def __init__(self, maxNumbers: int):
        self.unassigned = set()
        self.numbers = deque()
        for i in range(0, maxNumbers):
            self.unassigned.add(i)
            self.numbers.append(i)

    def get(self) -> int:
        if len(self.unassigned) == 0:
            return -1 # no available slot left
        number = self.numbers.popleft()
        self.unassigned.remove(number)
        return number

        # or can use self.unassigned.pop() -> remove randome element in the hashset.
        

    def check(self, number: int) -> bool:
        return number in self.unassigned

    def release(self, number: int) -> None:
        if number not in self.unassigned:
            self.unassigned.add(number)
            self.numbers.append(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)