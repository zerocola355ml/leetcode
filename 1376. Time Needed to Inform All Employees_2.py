# 350ms, 23.66%
# DFS, recursive

class Solution:
    def numOfMinutes(self, n, headID, manager, informTime):
        from collections import defaultdict

        graph = defaultdict(list)
        for i, m in enumerate(manager):
            if m != -1:
                graph[m].append(i)

        def dfs(node):
            if not graph[node]:  # leaf node
                return 0
            max_time = 0
            for emp in graph[node]:
                max_time = max(max_time, dfs(emp))
            return informTime[node] + max_time

        return dfs(headID)

