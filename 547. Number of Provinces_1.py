# 268ms, 5.31%
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        province = 0

        def dfs(i, j):
            if i > j:
                i, j = j, i
            if isConnected[i][j] == 1:
                isConnected[i][j] = 0
                for k in range(len(isConnected)):
                    dfs(i, k)
                    dfs(j, k)

        for i in range(len(isConnected)):
            for j in range(i, len(isConnected)):
                if isConnected[i][j] == 1:
                    province += 1
                    dfs(i, j)

        return province
