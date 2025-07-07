# 190ms, 67.97%
# DFS, Recursive

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))

        visited = [False] * n

        def dfs(node):
            visited[node] = True
            count = 0
            for nei, needs_change in graph[node]:
                if not visited[nei]:
                    count += needs_change
                    count += dfs(nei)
            return count

        return dfs(0)
