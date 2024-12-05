#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid"""
    rows = len(grid)
    cols = len(grid[0])
    edges = 0
    size = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                size += 1
                if (j > 0 and grid[i][j - 1] == 1):
                    edges += 1
                if (i > 0 and grid[i - 1][j] == 1):
                    edges += 1
    return ((size * 4) - (edges * 2))
