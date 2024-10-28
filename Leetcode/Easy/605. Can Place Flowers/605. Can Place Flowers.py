class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0: return True
        for i in range(len(flowerbed)):
            if flowerbed[i]: continue
            empty_left = True if (i == 0 or flowerbed[i-1] == 0) else False
            empty_right = True if (i == len(flowerbed) - 1 or flowerbed[i+1] == 0) else False
            if empty_left and empty_right:
                n -= 1
                flowerbed[i] = 1
            if n == 0: return True
        return False