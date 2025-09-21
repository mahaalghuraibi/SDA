# test_circle.py
import unittest
from src.circle import Circle, Sphere
import math

class TestCircle(unittest.TestCase):

    def test_radius(self):
        c = Circle(4)
        self.assertEqual(c.radius, 4)

    def test_diameter_getter_setter(self):
        c = Circle(4)
        self.assertEqual(c.diameter, 8)
        c.diameter = 10
        self.assertEqual(c.radius, 5)
        self.assertEqual(c.diameter, 10)

    def test_area(self):
        c = Circle(2)
        self.assertAlmostEqual(c.area, math.pi * 2**2)

    def test_from_diameter(self):
        c = Circle.from_diameter(8)
        self.assertEqual(c.radius, 4)
        self.assertEqual(c.diameter, 8)

    def test_str_repr(self):
        c = Circle(4)
        self.assertEqual(str(c), "Circle with radius: 4.000000")
        self.assertEqual(repr(c), "Circle(4)")
        d = eval(repr(c))
        self.assertEqual(d.radius, 4)

    def test_add_mul(self):
        c1 = Circle(2)
        c2 = Circle(4)
        self.assertEqual((c1 + c2).radius, 6)
        self.assertEqual((c2 * 3).radius, 12)
        self.assertEqual((3 * c2).radius, 12)

    def test_comparison_sorting(self):
        circles = [Circle(i) for i in [6, 7, 8, 4, 0, 2, 3, 5, 9, 1]]
        circles.sort()
        self.assertEqual([c.radius for c in circles], list(range(10)))

    def test_equality(self):
        c1 = Circle(4)
        c2 = Circle(4)
        c3 = Circle(5)
        self.assertTrue(c1 == c2)
        self.assertFalse(c1 == c3)
        self.assertTrue(c1 < c3)
        self.assertTrue(c3 > c2)

class TestSphere(unittest.TestCase):

    def test_str_repr(self):
        s = Sphere(5)
        self.assertEqual(str(s), "Sphere with radius: 5.000000")
        self.assertEqual(repr(s), "Sphere(5)")

    def test_area_volume(self):
        s = Sphere(3)
        self.assertAlmostEqual(s.area, 4 * math.pi * 3**2)
        self.assertAlmostEqual(s.volume, 4/3 * math.pi * 3**3)

    def test_add_sort(self):
        s1 = Sphere(2)
        s2 = Sphere(3)
        s3 = Sphere(1)
        spheres = [s1, s2, s3]
        spheres.sort()
        self.assertEqual([s.radius for s in spheres], [1,2,3])
        s4 = s1 + s2
        self.assertEqual(s4.radius, 5)

    def test_from_diameter(self):
        s = Sphere.from_diameter(8)
        self.assertIsInstance(s, Sphere)
        self.assertEqual(s.radius, 4)

if __name__ == '__main__':
    unittest.main()