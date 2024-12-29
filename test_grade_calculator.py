import unittest
from grade_calculator import calculate_grade

class TestGradeCalculator(unittest.TestCase):
    def test_valid_grades(self):
        # Test valid grades
        self.assertEqual(calculate_grade(95), "A")
        self.assertEqual(calculate_grade(85), "B")
        self.assertEqual(calculate_grade(75), "C")
        self.assertEqual(calculate_grade(65), "D")
        self.assertEqual(calculate_grade(50), "F")

    def test_boundary_conditions(self):
        # Test boundary grades
        self.assertEqual(calculate_grade(90), "A")
        self.assertEqual(calculate_grade(80), "B")
        self.assertEqual(calculate_grade(70), "C")
        self.assertEqual(calculate_grade(60), "D")
        self.assertEqual(calculate_grade(0), "F")

    def test_invalid_grades(self):
        # Test invalid grades
        self.assertEqual(calculate_grade(-10), "Invalid Score")
        self.assertEqual(calculate_grade(110), "Invalid Score")

if __name__ == "__main__":
    unittest.main()
