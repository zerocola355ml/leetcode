# 279ms, 57.35%
# BFS

class Solution:
    def numOfMinutes(self, n, headID, manager, informTime):
        graph = defaultdict(list)

        for emp, m in enumerate(manager):
            if m != -1:
                graph[m].append(emp)

        q = deque([(headID, 0)])  # (node, time)
        max_time = 0

        while q:
            node, time = q.popleft()
            max_time = max(max_time, time)
            for nei in graph[node]:
                q.append((nei, time + informTime[node]))

        return max_time

