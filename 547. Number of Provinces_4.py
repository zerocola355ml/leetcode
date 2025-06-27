# 3ms, 89.46%
# Union-Find (Disjoint Set Union)
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parent = list(range(len(isConnected)))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                parent[rootX] = rootY

        for i in range(len(isConnected)):
            for j in range(i + 1, len(isConnected)):
                if isConnected[i][j] == 1:
                    union(i, j)

        return len(set(find(i) for i in range(len(isConnected))))