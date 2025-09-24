# -----------------------------------------------------------------
# Challenge: 14_number_of_islands
# Prompt:
# You are given a 2D grid (list of lists) representing a map of '1's (land) and '0's (water).  
# An island is a group of connected '1's horizontally or vertically (not diagonally).  
# Write a function called `number_of_islands` that counts the number of islands in the grid.
#
# Example input:
# grid = [
#     ["1","1","0","0","0"],
#     ["1","1","0","0","0"],
#     ["0","0","1","0","0"],
#     ["0","0","0","1","1"]
# ]
#
# Example function call:
# number_of_islands(grid)  # returns 3
#
# Constraints:
# - The grid can be any size (MxN).
# - The grid contains only '1' or '0'.
# -----------------------------------------------------------------
def number_of_islands(grid):
    # عدد الصفوف والأعمدة
    rows = len(grid)
    cols = len(grid[0])
    
    def sink_island(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
            return
        grid[r][c] = "0"  
        sink_island(r+1, c)
        sink_island(r-1, c)
        sink_island(r, c+1)
        sink_island(r, c-1)

    # العداد
    island_count = 0
    
    # نمر على كل خلية
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                island_count += 1
                sink_island(r, c)
    
    return island_count


grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]

print(number_of_islands(grid))  
