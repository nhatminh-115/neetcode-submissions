class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        visited = set()
        pac = set()
        atl = set()

        def dfs(r,c, visited, prev):
            if r < 0 or r >= rows or c < 0 or c >= cols or heights[r][c] < prev or (r,c) in visited:
                return
            
            visited.add((r, c))

            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        # cạnh trên chạm Pacific
        # cạnh dưới chạm Atlantic
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        # cạnh trái chạm Pacific
        # cạnh phải chạm Atlantic
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        # lấy những ô xuất hiện trong cả 2 set
        return list(pac & atl)