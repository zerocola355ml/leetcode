# 151ms, 91.49%
# DFS, Stack

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph_from = collections.defaultdict(list)
        graph_to = collections.defaultdict(list)
        visited = [False] * n
        change = 0
        stack = [0]

        for a, b in connections:
            graph_from[a].append(b)
            graph_to[b].append(a)

        while stack:
            node = stack.pop()
            visited[node] = True
            for to in graph_from[node]:
                if visited[to] is False:
                    change += 1
                    stack.append(to)
            for from_ in graph_to[node]:
                if visited[from_] is False:
                    stack.append(from_)

        return change
