class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def dfs(room):
            visited.add(room)

            for next_room in rooms[room]:
                if next_room not in visited:
                    dfs(next_room)

        dfs(0)
        return len(visited) == len(rooms)