import unittest
from PY_code_challenges import c14_number_of_islands

if __name__ == "__main__":
    unittest.main()


class TestNumberOfIslands(unittest.TestCase):
    # -----------------------------------------------------------------
    # Test 1: Example from prompt
    # Grid contains 3 islands: top-left 2x2, middle single cell, bottom-right 2 cells
    # -----------------------------------------------------------------
    def test_example_grid(self):
        grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
        result = c14_number_of_islands.number_of_islands(grid)
        self.assertEqual(result, 3)

    # -----------------------------------------------------------------
    # Test 2: Single island occupying the entire grid
    # -----------------------------------------------------------------
    def test_single_large_island(self):
        grid = [
            ["1","1"],
            ["1","1"]
        ]
        result = c14_number_of_islands.number_of_islands(grid)
        self.assertEqual(result, 1)

    # -----------------------------------------------------------------
    # Test 3: Grid with no land
    # Should return 0
    # -----------------------------------------------------------------
    def test_no_land(self):
        grid = [
            ["0","0","0"],
            ["0","0","0"]
        ]
        result = c14_number_of_islands.number_of_islands(grid)
        self.assertEqual(result, 0)

    # -----------------------------------------------------------------
    # Test 4: Grid with diagonal "islands" (should not count diagonals)
    # Diagonal 1s are separate islands
    # -----------------------------------------------------------------
    def test_diagonal_islands(self):
        grid = [
            ["1","0","0"],
            ["0","1","0"],
            ["0","0","1"]
        ]
        result = c14_number_of_islands.number_of_islands(grid)
        self.assertEqual(result, 3)

    # -----------------------------------------------------------------
    # Test 5: Large grid with multiple islands
    # Ensures algorithm handles bigger input
    # -----------------------------------------------------------------
    def test_large_grid(self):
        grid = [
            ["1","0","1","0","1"],
            ["0","1","0","1","0"],
            ["1","0","1","0","1"],
            ["0","1","0","1","0"]
        ]
        result = c14_number_of_islands.number_of_islands(grid)
        self.assertEqual(result, 10)

    # -----------------------------------------------------------------
    # Test 6: Single cell island
    # Grid with one land cell
    # -----------------------------------------------------------------
    def test_single_cell_island(self):
        grid = [["1"]]
        result = c14_number_of_islands.number_of_islands(grid)
        self.assertEqual(result, 1)

    # -----------------------------------------------------------------
    # Test 7: Empty grid
    # Should return 0
    # -----------------------------------------------------------------
    def test_empty_grid(self):
        grid = []
        result = c14_number_of_islands.number_of_islands(grid)
        self.assertEqual(result, 0)
