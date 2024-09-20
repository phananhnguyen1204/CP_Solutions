class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        q = deque()
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1
        
        for i in range(numCourses):
            if indegree[i] == 0: q.append(i)
        
        cnt = 0
        while q:
            course = q[0]
            q.popleft()
            cnt += 1
            for next_course in adj[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    q.append(next_course)
        return True if cnt == numCourses else False    
        
            