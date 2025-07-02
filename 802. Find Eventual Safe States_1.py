# 27ms, 87.64%
# DFS + 방문 배열

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = [0] * len(graph)  # 0=unvisited, 1=visiting, 2=safe

        def has_cycle(v):
            if visited[v] == 1:
                return True
            if visited[v] == 2:
                return False
            visited[v] = 1
            for nei in graph[v]:
                if has_cycle(nei) is True:
                    return True
            visited[v] = 2
            return False

        result = []
        for i in range(len(graph)):
            if has_cycle(i) is False:
                result.append(i)

        return result