from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = '0'  

            while q:
                x, y = q.popleft()

                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '1':
                        grid[nx][ny] = '0'
                        q.append((nx, ny))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    bfs(i, j)
                    islands += 1

        return islands