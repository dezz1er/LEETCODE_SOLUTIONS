import collections
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]],
                  source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, visited):
            if node == destination:
                return True
            visited.add(node)
            for ng in graph[node]:
                if ng not in visited:
                    if dfs(ng, visited):
                        return True
            return False
        visited = set()
        return dfs(source, visited)
