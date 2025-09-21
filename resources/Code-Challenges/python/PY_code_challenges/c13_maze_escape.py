# -----------------------------------------------------------------
# Challenge: 13_maze_escape
# Prompt:
# You are given a 2D list (`maze`) representing a rectangular maze, where:
# - 'S' represents the starting point,
# - 'E' represents the exit,
# - '0' represents an open path,
# - '1' represents a wall.
#
# Write a function called `maze_escape` that determines whether there is a path from 'S' to 'E'.  
# You can move up, down, left, or right, but cannot move diagonally.  
#
# The function should return True if a path exists, or False otherwise.
#
# Example input:
# maze = [
#     ['S', '0', '1', '0'],
#     ['1', '0', '1', '0'],
#     ['1', '0', '0', '0'],
#     ['1', '1', '1', 'E']
# ]
#
# Example function call:
# maze_escape(maze)  # returns True
#
# Constraints:
# - You may assume there is exactly one 'S' and one 'E' in the maze.
# - The maze may be any rectangular size.
# -----------------------------------------------------------------
def maze_escape(maze):
    start = None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start = (i, j)
                break
        if start:
            break

    if start is None:
        return False

    to_visit = [start]
    visited = set([start])

    while to_visit:
        x, y = to_visit.pop()  

        if maze[x][y] == 'E':
            return True

        moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        for nx, ny in moves:
            if (0 <= nx < len(maze) and 0 <= ny < len(maze[0])  # داخل حدود المصفوفة
                and maze[nx][ny] != '1'                         # مش جدار
                and (nx, ny) not in visited):                   # مش مكرر
                to_visit.append((nx, ny))
                visited.add((nx, ny))

    return False


maze = [
    ['S', '0', '1', '0'],
    ['1', '0', '1', '0'],
    ['1', '0', '0', '0'],
    ['1', '1', '1', 'E']
]

print(maze_escape(maze))  
