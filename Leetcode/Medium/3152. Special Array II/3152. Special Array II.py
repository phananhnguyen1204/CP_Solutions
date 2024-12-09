class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)

        check = [0] * n
        cnt = 1
        check[0] = cnt
        answer = []

        for i in range(1, n):
            if nums[i] % 2 != nums[i-1] % 2:
                check[i] = cnt
            else:
                cnt += 1
                check[i] = cnt

        for query in queries:
            start, end = query
            
            if check[start] == check[end]:
                answer.append(True)
            else:
                answer.append(False)
        
        return answer
                