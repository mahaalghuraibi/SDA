import unittest
from PY_code_challenges import c13_maze_escape

if __name__ == "__main__":
    unittest.main()


class TestMazeEscape(unittest.TestCase):
    # -----------------------------------------------------------------
    # Test 1: Maze with a clear path from 'S' to 'E'
    # -----------------------------------------------------------------
    def test_maze_with_path(self):
        maze = [
            ['S', '0', '1', '0'],
            ['1', '0', '1', '0'],
            ['1', '0', '0', '0'],
            ['1', '1', '1', 'E']
        ]
        result = c13_maze_escape.maze_escape(maze)
        self.assertTrue(result)

    # -----------------------------------------------------------------
    # Test 2: Maze with no path to exit
    # -----------------------------------------------------------------
    def test_maze_no_path(self):
        maze = [
            ['S', '1', '1'],
            ['1', '1', '1'],
            ['1', '1', 'E']
        ]
        result = c13_maze_escape.maze_escape(maze)
        self.assertFalse(result)

    # -----------------------------------------------------------------
    # Test 3: Maze where 'S' is adjacent to 'E'
    # Should return True
    # -----------------------------------------------------------------
    def test_start_adjacent_to_exit(self):
        maze = [
            ['S', 'E'],
            ['1', '1']
        ]
        result = c13_maze_escape.maze_escape(maze)
        self.assertTrue(result)

    # -----------------------------------------------------------------
    # Test 4: Larger maze with a winding path
    # Tests complexity and ensures traversal algorithm works
    # -----------------------------------------------------------------
    def test_larger_maze(self):
        maze = [
            ['S', '0', '1', '0', '0', '0'],
            ['1', '0', '1', '0', '1', '0'],
            ['1', '0', '0', '0', '1', '0'],
            ['1', '1', '1', '0', '1', 'E'],
            ['0', '0', '0', '0', '0', '1']
        ]
        result = c13_maze_escape.maze_escape(maze)
        self.assertTrue(result)

    # -----------------------------------------------------------------
    # Test 5: Empty maze (edge case)
    # No start or exit; should return False
    # -----------------------------------------------------------------
    def test_empty_maze(self):
        maze = []
        result = c13_maze_escape.maze_escape(maze)
        self.assertFalse(result)

    # -----------------------------------------------------------------
    # Test 6: Maze where start is blocked by walls
    # -----------------------------------------------------------------
    def test_start_blocked(self):
        maze = [
            ['S', '1', '1'],
            ['1', '0', 'E']
        ]
        result = c13_maze_escape.maze_escape(maze)
        self.assertFalse(result)
