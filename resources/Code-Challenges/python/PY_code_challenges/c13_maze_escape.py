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

    to_visit = [start]
    visited = set()

    while to_visit:
        x, y = to_visit.pop()  

        if maze[x][y] == 'E':   
            return True

        if (x, y) not in visited:
            visited.add((x, y))

            if x > 0 and maze[x-1][y] != '1':
                to_visit.append((x-1, y))
            if x < len(maze)-1 and maze[x+1][y] != '1':
                to_visit.append((x+1, y))
            if y > 0 and maze[x][y-1] != '1':
                to_visit.append((x, y-1))
            if y < len(maze[0])-1 and maze[x][y+1] != '1':
                to_visit.append((x, y+1))

    return False
