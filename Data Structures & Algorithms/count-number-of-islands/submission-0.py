class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if (grid[i][j] == "1"):
                    count += 1

                    def DFS(x, y) -> None:

                        if (x >= len(grid) or x < 0 or y >= len(grid[0]) or y < 0):
                            return
                        elif (grid[x][y] == "0"):
                            return
                        else:
                            grid[x][y] = "0"
                            DFS(x + 1, y)
                            DFS(x - 1, y)
                            DFS(x, y + 1)
                            DFS(x, y - 1)
                    
                    DFS(i, j)

        return count