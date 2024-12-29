class TwoSum:

    def __init__(self):
        self.list = []

    def add(self, number: int) -> None:
        self.list.append(number)

    def find(self, value: int) -> bool:
        if not self.list: return False

        hash_set = set()
        for num in self.list:
            if value - num in hash_set:
                return True
            hash_set.add(num)
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)