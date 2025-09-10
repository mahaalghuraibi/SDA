import unittest
from PY_code_challenges import c15_merge_intervals

if __name__ == "__main__":
    unittest.main()


class TestMergeIntervals(unittest.TestCase):
    # -----------------------------------------------------------------
    # Test 1: Example from prompt
    # Overlapping intervals [[1,3],[2,6]] should merge into [1,6]
    # -----------------------------------------------------------------
    def test_example_overlap(self):
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        expected = [[1,6],[8,10],[15,18]]
        result = c15_merge_intervals.merge_intervals(intervals)
        self.assertEqual(result, expected)

    # -----------------------------------------------------------------
    # Test 2: Intervals that are exactly adjacent
    # [[1,4],[4,5]] should merge into [1,5]
    # -----------------------------------------------------------------
    def test_adjacent_intervals(self):
        intervals = [[1,4],[4,5]]
        expected = [[1,5]]
        result = c15_merge_intervals.merge_intervals(intervals)
        self.assertEqual(result, expected)

    # -----------------------------------------------------------------
    # Test 3: Intervals that do not overlap
    # Should remain unchanged but sorted
    # -----------------------------------------------------------------
    def test_no_overlap(self):
        intervals = [[5,6],[1,2],[8,10]]
        expected = [[1,2],[5,6],[8,10]]
        result = c15_merge_intervals.merge_intervals(intervals)
        self.assertEqual(result, expected)

    # -----------------------------------------------------------------
    # Test 4: Single interval
    # Should return the same interval
    # -----------------------------------------------------------------
    def test_single_interval(self):
        intervals = [[1,3]]
        expected = [[1,3]]
        result = c15_merge_intervals.merge_intervals(intervals)
        self.assertEqual(result, expected)

    # -----------------------------------------------------------------
    # Test 5: Empty list
    # Should return an empty list
    # -----------------------------------------------------------------
    def test_empty_list(self):
        intervals = []
        expected = []
        result = c15_merge_intervals.merge_intervals(intervals)
        self.assertEqual(result, expected)

    # -----------------------------------------------------------------
    # Test 6: Fully overlapping intervals
    # [[1,10],[2,3],[4,8]] should merge into [1,10]
    # -----------------------------------------------------------------
    def test_fully_overlapping(self):
        intervals = [[1,10],[2,3],[4,8]]
        expected = [[1,10]]
        result = c15_merge_intervals.merge_intervals(intervals)
        self.assertEqual(result, expected)

    # -----------------------------------------------------------------
    # Test 7: Intervals unsorted
    # Function should sort them automatically
    # -----------------------------------------------------------------
    def test_unsorted_intervals(self):
        intervals = [[5,7],[1,3],[2,6]]
        expected = [[1,7]]
        result = c15_merge_intervals.merge_intervals(intervals)
        self.assertEqual(result, expected)
