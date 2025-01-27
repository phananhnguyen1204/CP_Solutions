class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        """
        greedy? -> invite people with the most favorite -> to maximize # of employees -> No
        directed graph?

        finding the cycle of the directed graph, since people need to sit in the cycle
        -> find the largest cycle
        cycle with size == 2 (people are mutually friended) (we can treated as one unit) -> checking if one of the node is the end node of the chain or not -> use reverse graph

        1. find max_len_cycle
            -visited set(): keep track of all visited person
            - path set(): to check if we have cycle or not
        2. find cycle with size equal 2:
            from one of 2 nodes -> calculate len of the chain using reverse graph
        """

        n = len(favorite)
        
        def find_max_len_cycle():
            visited = set()
            max_len_cycle = 0
            # i: person
            for i in range(n):
                # we already build this chain
                if i in visited: continue
                path = set()
                begin_person = i
                curr_person = i

                while curr_person not in visited:
                    visited.add(curr_person)
                    path.add(curr_person)
                    curr_person = favorite[curr_person]
                # found cycle
                if curr_person in path:
                    len_cycle = len(path)
                    while begin_person != curr_person:
                        begin_person = favorite[begin_person]
                        len_cycle -= 1
                    max_len_cycle = max(max_len_cycle, len_cycle) 
            return max_len_cycle

        

        def find_mutal_cycle():
            reverse_graph = defaultdict(list)
            max_len = 0
            seen = set()
            mutal_pairs = set()
            for i in range(n):
                reverse_graph[favorite[i]].append(i)


            def bfs(start):
                q = deque()
                q.append((start, 0))
                chain_len = 0

                while q:
                    node, dist = q.popleft()
                    chain_len = max(chain_len, dist)
                    for neighbor in reverse_graph[node]:
                        if neighbor not in seen:
                            q.append((neighbor, dist + 1))
                            seen.add(neighbor)

                return chain_len
                    
            #i - person
            for i in range(n):
                # found mutal favorite person
                if i == favorite[favorite[i]]:
                    
                    curr_person, next_person = i, favorite[i]
                    seen = set()
                    seen.add(curr_person)
                    seen.add(next_person)
                    # print(bfs(curr_person))
                    # print(bfs(next_person))
                    max_len += bfs(curr_person) + bfs(next_person) + 2

            return max_len // 2
        a = find_mutal_cycle()
        b = find_max_len_cycle()
        return max(a, b)

            


                    
               
                
        

