import unittest
from PY_code_challenges import c11_student_grade_report

if __name__ == "__main__":
    unittest.main()


class TestStudentGradeReport(unittest.TestCase):
    # -----------------------------------------------------------------
    # Test 1: Multiple students with normal score lists
    # Standard case: ensures average, high, low, and letter grades are calculated correctly.
    # -----------------------------------------------------------------
    def test_multiple_students(self):
        students = {
            "Alice": [95, 85, 92],
            "Bob": [70, 80, 65],
            "Charlie": [50, 60, 55]
        }
        result = c11_student_grade_report.student_grade_report(students)
        expected = (
            "Alice: Average = 90.67, High = 95, Low = 85, Grade = A\n"
            "Bob: Average = 71.67, High = 80, Low = 65, Grade = C\n"
            "Charlie: Average = 55.0, High = 60, Low = 50, Grade = F"
        )
        self.assertEqual(result, expected)

    # -----------------------------------------------------------------
    # Test 2: Single student
    # Ensures function works with only one student in the dictionary.
    # -----------------------------------------------------------------
    def test_single_student(self):
        students = {"David": [88, 92, 79]}
        result = c11_student_grade_report.student_grade_report(students)
        expected = "David: Average = 86.33, High = 92, Low = 79, Grade = B"
        self.assertEqual(result, expected)

    # -----------------------------------------------------------------
    # Test 3: Empty dictionary
    # Should return an empty string if no students are provided.
    # -----------------------------------------------------------------
    def test_empty_students(self):
        students = {}
        result = c11_student_grade_report.student_grade_report(students)
        expected = ""
        self.assertEqual(result, expected)

    # -----------------------------------------------------------------
    # Test 4: Student with empty score list
    # Should handle gracefully. Could return None, 0, or custom message.
    # Here, assuming average=0, high=None, low=None, grade=F.
    # -----------------------------------------------------------------
    def test_empty_score_list(self):
        students = {"Eve": []}
        result = c11_student_grade_report.student_grade_report(students)
        expected = "Eve: Average = 0.0, High = None, Low = None, Grade = F"
        self.assertEqual(result, expected)

    # -----------------------------------------------------------------
    # Test 5: Student with perfect scores
    # Ensures that boundary values (100) yield correct letter grade A.
    # -----------------------------------------------------------------
    def test_perfect_scores(self):
        students = {"Frank": [100, 100, 100]}
        result = c11_student_grade_report.student_grade_report(students)
        expected = "Frank: Average = 100.0, High = 100, Low = 100, Grade = A"
        self.assertEqual(result, expected)
