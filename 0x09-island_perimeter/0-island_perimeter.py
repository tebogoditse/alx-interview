#!/usr/bin/python3
"""Returns the perimeter of the island described in grid"""


def island_perimeter(grid):
    width = len(grid[0])
    height = len(grid)
    rows = 0
    cols = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                cols = cols + 1
                if (j > 0 and grid[i][j - 1] == 1):
                    rows = rows + 1
                if (i > 0 and grid[i - 1][j] == 1):
                    rows = rows + 1
    return ((cols * 4) - (rows * 2))
