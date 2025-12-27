class Solution(object):
    def largestLocal(self, grid):
        n = len(grid)
        result = []


        for i in range(n - 2):
            row = []
            for j in range(n - 2):
                max_val = 0
 
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        if grid[x][y] > max_val:
                            max_val = grid[x][y]

                row.append(max_val)
            result.append(row)

        return result