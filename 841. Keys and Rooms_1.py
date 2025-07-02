# 0ms, 100.00%
# BFS

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        unlocked = [False] * len(rooms)
        unlocked[0] = True

        q = deque([0])
        while q:
            room = q.popleft()
            for key in rooms[room]:
                if not unlocked[key]:
                    unlocked[key] = True
                    q.append(key)

        return all(unlocked)
