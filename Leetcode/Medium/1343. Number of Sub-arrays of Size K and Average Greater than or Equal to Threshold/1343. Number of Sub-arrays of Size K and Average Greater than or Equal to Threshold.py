class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        curr_sum = sum(arr[:k-1])
        for r in range(k-1, len(arr)):
            curr_sum += arr[r]
            if (curr_sum / k) >= threshold: res += 1
            curr_sum -= arr[r-k+1]
        return res