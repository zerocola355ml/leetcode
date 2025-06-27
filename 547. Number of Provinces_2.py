# 3ms, 89.46%
# DFS
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n

        def dfs(i):
            for j in range(n):
                if isConnected[i][j] == 1 and not visited[j]:
                    visited[j] = True
                    dfs(j)

        province = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                province += 1
        return province
