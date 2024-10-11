class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for x in asteroids:
            while stack and x < 0 and stack[-1] > 0:
               diff = stack[-1] + x
               if diff > 0:
                x = 0
                break
               elif diff == 0: 
                x = 0
                stack.pop()
               else: 
                stack.pop()
            if x:
                stack.append(x)
        
        return stack
