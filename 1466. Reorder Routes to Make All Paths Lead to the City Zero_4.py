# 12ms, 99.74%
# Iterative Edge Filtering with Visited Expansion

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = set()
        visited.add(0)
        count = 0

        while len(visited) < n:
            check = []
            for path in connections:
                if path[1] in visited:
                    visited.add(path[0])

                elif path[0] in visited:
                    visited.add(path[1])
                    count += 1

                else:
                    check.append(path)

            connections = check[::-1] # 역순으로 하면 최악의 경우를 피함.

        return count