import collections
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))
            while q:
                row, col = q.popleft()
                direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in direction:
                    r, c = row + dr, col + dc
                    if (
                        r in range(rows) and c in range(cols) and grid[r][c] == "1"
                    ) and (r, c) not in visit:
                        q.append((r, c))
                        visit.add((r, c))

        rows, cols = len(grid), len(grid[0])
        visit = set()
        isisland = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visit:
                    bfs(i, j)
                    isisland += 1
        return isisland
