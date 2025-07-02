# 51ms, 51.75%
# BFS using Reverse Graph

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reverse_graph = [[] for _ in range(n)]
        out_degree = [0] * n

        for u in range(n):
            for v in graph[u]:
                reverse_graph[v].append(u)
            out_degree[u] = len(graph[u])

        q = deque([i for i in range(n) if out_degree[i] == 0])
        safe = [False] * n

        while q:
            node = q.popleft()
            safe[node] = True
            for prev in reverse_graph[node]:
                out_degree[prev] -= 1
                if out_degree[prev] == 0:
                    q.append(prev)

        return [i for i in range(n) if safe[i]]