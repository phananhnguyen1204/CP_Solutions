class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        prefix_sum = 0
        sorted_sum = 0
        chunks = 0

        for i, num in enumerate(arr):
            prefix_sum += num
            sorted_sum += i

            if prefix_sum == sorted_sum:
                chunks += 1

        return chunks
