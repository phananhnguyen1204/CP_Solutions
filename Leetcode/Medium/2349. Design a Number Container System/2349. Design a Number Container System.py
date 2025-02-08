
class NumberContainers:

    def __init__(self):
        """
        indexs: index -> number
        numbers: numer -> sorted list of index (from smallest to largest)
        numbers: tree map (since we want update index, and get the smallest index)
        """

        self.indexes = defaultdict(int)
        self.numbers = defaultdict(SortedSet) # numbers is map -> sortedset

    def change(self, index: int, number: int) -> None:
        if index not in self.indexes:
            self.indexes[index] = number
            self.numbers[number].add(index)
        else:
            prev_num = self.indexes[index]
            self.indexes[index] = number
            self.numbers[prev_num].discard(index)
            if not self.numbers[prev_num]:
                del self.numbers[prev_num]
            self.numbers[number].add(index)

    def find(self, number: int) -> int:
        if number not in self.numbers:
            return -1
        return self.numbers[number][0]
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)