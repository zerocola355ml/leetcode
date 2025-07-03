# 212ms, 89.07%
# DFS, memoization, top-down

class Solution:
    def numOfMinutes(self, n, headID, manager, informTime):
        memo = {}

        def dfs(emp):
            if emp == headID:
                return 0
            if emp in memo:
                return memo[emp]
            time = informTime[manager[emp]] + dfs(manager[emp])
            memo[emp] = time
            return time

        return max(dfs(i) for i in range(n))
