class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        check divisiable (has to use all the cards)
        card can have duplicate
        if yes -> sorting and check each group

        [1, 2, 2, 3, 3, 4, 6, 7, 8]
        """
        n = len(hand)
        if n % groupSize != 0: return False

        hand.sort()
        hand = deque(hand)

        freq = defaultdict(int)
        for num in hand:
            freq[num] += 1

        for num in hand:
            if freq[num] > 0:
                for j in range(groupSize):
                    if freq[num + j] == 0:
                        return False
                    freq[num + j] -= 1
        return True