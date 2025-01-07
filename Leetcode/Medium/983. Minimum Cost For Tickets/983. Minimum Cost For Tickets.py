class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        

        """
        dfs(curr_day) = cost[0] + dfs(i + 7)
        dfs(i)
        """
        last_day = max(days)
        memo = {}

        def dfs(curr_day):
            if curr_day > last_day:
                return 0
            if curr_day not in days:
                return dfs(curr_day + 1)
            
            if curr_day in memo:
                return memo[curr_day]
            
            one_day = costs[0] + dfs(curr_day + 1)
            seven_day = costs[1] + dfs(curr_day + 7)
            thirty_day = costs[2] + dfs(curr_day + 30)

            memo[curr_day] = min(one_day, seven_day, thirty_day)
            return memo[curr_day]

        return dfs(1)
                 

            