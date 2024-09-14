class RandomizedSet:

    def __init__(self):
        self.list = []
        self.dict = {}

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict: return False
        last, idx = self.list[-1], self.dict[val]
        self.list[idx], self.dict[last] = last, idx
        del self.dict[val]
        self.list.pop()
        return True

    def getRandom(self) -> int:
        return choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()