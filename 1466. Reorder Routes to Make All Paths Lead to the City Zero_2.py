# 166, 86.54%
# BFS

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append((b, 1))  # 변경 필요
            graph[b].append((a, 0))  # 변경 필요 없음

        visited = [False] * n
        queue = deque([0])
        change = 0

        while queue:
            node = queue.popleft()
            visited[node] = True
            for nei, needs_change in graph[node]:
                if not visited[nei]:
                    change += needs_change
                    queue.append(nei)

        return change

