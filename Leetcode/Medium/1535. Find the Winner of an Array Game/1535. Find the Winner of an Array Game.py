class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        winner = arr[0]
        max_element = max(arr)
        win_count = 0

        for i in range(1, len(arr)):
            if winner >= arr[i]:
                win_count += 1
            else: 
                win_count = 1
                winner = arr[i]
            if win_count == k or winner == max_element:
                return winner
