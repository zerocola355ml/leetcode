# 1ms, 85.74%
# BFS
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(lambda: {'red': [], 'blue': []})
        for u, v in redEdges:
            graph[u]['red'].append(v)
        for u, v in blueEdges:
            graph[u]['blue'].append(v)

        result = [-1] * n
        visited = [[False, False] for _ in range(n)]  # visited[node][0: red, 1: blue]

        q = deque()
        q.append((0, 0, None))  # node, steps, prev_color

        while q:
            node, steps, color = q.popleft()
            if result[node] == -1:
                result[node] = steps
            # 다음으로 갈 색상은 현재 색상과 반대
            for next_color in ('red', 'blue'):
                if next_color == color:
                    continue
                color_idx = 0 if next_color == 'red' else 1
                for nei in graph[node][next_color]:
                    if not visited[nei][color_idx]:
                        visited[nei][color_idx] = True
                        q.append((nei, steps + 1, next_color))

        return result