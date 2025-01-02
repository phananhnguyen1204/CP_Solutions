class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1

        while l < r:
            mid = (l + r) // 2
            if letters[mid] <= target:
                l = mid + 1
            else:
                r = mid

        return letters[r] if letters[r] > target else letters[0]