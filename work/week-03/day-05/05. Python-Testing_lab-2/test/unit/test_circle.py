import math
import unittest
from src import circle


class TestCircle(unittest.TestCase):

    def setUp(self):
        print("Setting up!")
        self.CONST_TEST_RADIUS = 5
        self.CONST_TEST_DIAMETER = 8

    def tearDown(self):
        print("Tearing down!\n")

    def test_circle_creation(self):
        pass

    def test_circle_property_diameter(self):
        pass

    def test_circle_set_diameter(self):
        pass

    def test_circle_area(self):
        pass

    def test_cls_method(self):
        pass

    def test_circle_str(self):
        pass

    def test_circle_repr(self):
        pass

    def test_circle_add(self):
        pass

    def test_circle_mult(self):
        pass

    def test_comparison_operators(self):
        pass

    def test_sphere_volume(self):
        pass

    def test_sphere_area(self):
        pass

    def test_sphere_add(self):
        pass

    def test_sphere_comparison_operators(self):
        pass


if __name__ == "__main__":
    unittest.main()
