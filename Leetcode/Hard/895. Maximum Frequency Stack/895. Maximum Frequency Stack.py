class FreqStack:

    """
    we need cnt frequency of element
    every operation is O(1)

    need hashmap to find the most frequent element and remove
    -> hashmap where key is a stack
    [1, 3, 3, 3]
    """

    def __init__(self):
        self.max_freq = 0
        self.freq = defaultdict(int)
        self.most_freq = defaultdict(list)
        

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.max_freq = max(self.max_freq, self.freq[val])
        self.most_freq[self.freq[val]].append(val)

    def pop(self) -> int:
        res = self.most_freq[self.max_freq].pop()
        self.freq[res] -= 1
        if not self.most_freq[self.max_freq]:
            self.max_freq -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()