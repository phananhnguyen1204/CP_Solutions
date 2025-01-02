class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1

        # Case 1: x <= arr[mid] <= arr[mid + k] -> move left
        # Case 2: arr[mid] <= x <= arr[mid + k] -> depend
        # Case 3: arr[mid] <= arr[mid + k] <= x -> move right

        #abs(x - arr[mid]) > abs(x - arr[mid + k]): move right

        # x - arr[mid] > arr[mid + k] - x: move right

        l, r = 0, len(arr) - k


        while l < r:
            mid = (l + r) // 2
            print(arr[mid])
            if x - arr[mid] > arr[mid + k] - x:
                l = mid + 1
            else:
                r = mid

        return arr[l : l + k]