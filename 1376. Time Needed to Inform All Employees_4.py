# 391ms, 13.53%
# DFS, bottom-up

class Solution:
    def numOfMinutes(self, n, headID, manager, informTime):
        from collections import defaultdict

        graph = defaultdict(list)
        for emp, m in enumerate(manager):
            if m != -1:
                graph[m].append(emp)

        dp = [0] * n

        def dfs(emp):
            if not graph[emp]:
                return 0
            if dp[emp] > 0:
                return dp[emp]
            dp[emp] = informTime[emp] + max(dfs(e) for e in graph[emp])
            return dp[emp]

        return dfs(headID)

