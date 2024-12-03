#!/usr/bin/python3
"""Defines a function to compute the perimeter of an island in a grid."""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island.

    The grid represents water by 0 and land by 1.

    Args:
        grid (list of list of int): A grid where 1 represents
        land and 0 represents water.

    Returns:
        int: The perimeter of the island defined in the grid.
    """
    rows = len(grid)  # Number of rows in the grid
    cols = len(grid[0])  # Number of columns in the grid
    adjacent_count = 0  # Tracks the number of shared edges between land cells
    land_count = 0  # Tracks the total number of land cells

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:  # Check if the current cell is land
                land_count += 1

                # Check if the left neighbor is land
                if col > 0 and grid[row][col - 1] == 1:
                    adjacent_count += 1

                # Check if the top neighbor is land
                if row > 0 and grid[row - 1][col] == 1:
                    adjacent_count += 1

    # Calculate perimeter: each land cell
    # contributes 4 sides minus twice the shared edges
    return land_count * 4 - adjacent_count * 2
